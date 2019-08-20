# -*- coding: utf-8 -*-
import datetime

from selenium import webdriver
import pandas as pd
import requests
import abc

from stocks.constants import chromedriver_path


class AbsStockDataFetcher(metaclass=abc.ABCMeta):
    """
    Abstract stock data fetcher class
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_historical_data(self, symbol, start_date, end_date):
        """
        :param symbol:
        :param start: start date, format: yyyy-mm-dd
        :param end: end date, format: yyyy-mm-dd
        :return: data
        """
        pass


class YahooFinanceStockDataFetcher(AbsStockDataFetcher):

    def __init__(self):
        super().__init__()

    def get_historical_data(self, symbol, start, end):
        """
        :param symbol:
        :param start: start date, format: yyyy-mm-dd
        :param end: end date, format: yyyy-mm-dd
        :return: df
        """
        response_json = self._download_symbol_data(symbol, start, end)
        df = self._convert_json_data_to_df(response_json)
        return df

    def _download_symbol_data(self, symbol, start, end):
        """

        :param symbol:
        :param start: start date, format: yyyy-mm-dd
        :param end: end date, format: yyyy-mm-dd
        :return: the response in json format
        """
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        start_date_timestamp_str = round(start_date.timestamp())
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        end_date_timestamp_str = round(end_date.timestamp())
        url = ('https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?symbol={symbol}'
               '&period1={start}&period2={end}&interval=1d&'
               'includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&'
               'region=US&crumb=t5QZMhgytYZ&corsDomain=finance.yahoo.com'
               ).format(symbol=symbol, start=start_date_timestamp_str, end=end_date_timestamp_str)
        response_json = requests.get(url).json()
        return response_json

    def _convert_json_data_to_df(self, response_json):
        """

        :param response_json:
        :return: df with quote values by date
        """
        data_json = response_json['chart']['result'][0]
        quote_data = data_json["indicators"]["quote"][0]
        df = pd.DataFrame(quote_data)
        try:
            quote_date = [datetime.datetime.fromtimestamp(i).strftime("%Y-%m-%d") for i in data_json["timestamp"]]
            adjclose = data_json["indicators"]["adjclose"][0]["adjclose"]
            df["date"] = quote_date
            df["adj_close"] = adjclose
            df["symbol"] = data_json["meta"]["symbol"]
            df = df.loc[:, ["adj_close", "close", "date", "high", "low", "open", "symbol", "volume"]]
        except KeyError:
            print("Data does not exist for stock {}?".format(symbol))
        return df


class InvestingComSp500TodayFetcher(AbsStockDataFetcher):
    """
    Fetch the today's quote of Sp500 stocks
    """

    def __init__(self):
        self.website_url = 'https://www.investing.com/indices/investing.com-us-500-components'
        self.driver = webdriver.Chrome(chromedriver_path)
        super().__init__()

    def get_historical_data(self):
        self._download_barchart_page()
        data = self._parse_barchart_page()
        return data

    def _download_barchart_page(self):
        self.driver.get(self.website_url)

    def _parse_barchart_page(self):
        """
        Parse the html downloaded from investing.com and return a dict for the sp500 companies
        :return:
        """
        data_dict = {}
        data_table = self.driver.find_element_by_xpath('//*[@id="cr1"]/tbody')
        trs = data_table.find_elements_by_tag_name('tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
            temp_stock_values_dict = {}
            for td in tds:
                if td.get_attribute("class") == 'bold left noWrap elp plusIconTd':
                    company_name = td.text
                else:
                    stock_attribute = td.get_attribute("class")
                    stock_attribute = stock_attribute.strip()
                    stock_value = td.text
                    temp_stock_values_dict[stock_attribute] = stock_value
            data_dict[company_name] = temp_stock_values_dict
        return data_dict

    def _convert_data_to_df(self):
        pass
