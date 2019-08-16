# -*- coding: utf-8 -*-
import datetime

import pandas as pd
import requests
import abc

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
        pass

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
        print(url)
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
        quote_date = [datetime.datetime.fromtimestamp(i).strftime("%Y-%m-%d") for i in data_json["timestamp"]]
        df["date"] = quote_date
        return df

if __name__ == "__main__":
    symbol = "SQ"
    start = "2019-01-01"
    end = "2019-02-01"
    yahoo_finance = YahooFinanceStockDataFetcher()
    df = yahoo_finance.get_historical_data(symbol, start, end)
    print(df)

