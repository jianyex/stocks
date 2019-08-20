import time
import datetime
import random

from stocks.stock_data_fetcher import InvestingComSp500TodayFetcher, YahooFinanceStockDataFetcher
from stocks.sqlite_connector import SqliteConnector
from stocks.constants import db_file_path, SYMBOLS


def fetch_daily_sp500_quotes_from_investing_com():
    """
    Download and parse the stock quotes data for today from investing.com
    :return: historical_data, as json string
    """
    investing_com_data_fetcher = InvestingComSp500TodayFetcher()
    historical_data = investing_com_data_fetcher.get_historical_data()
    return historical_data


def save_quotes_from_investing_com_to_db(raw_json_data, conn):
    """
    save the today's sp500 raw data to database
    :param raw_json_data:
    :param conn:
    :return:
    """
    raw_json_data_str = str(raw_json_data)
    date = raw_json_data["3M"]['pid-277-time']
    records = [{"raw_json_data": raw_json_data_str, "date": date}]
    conn.insert_records(table="investing_com_sp500_today", records=records)


def fetch_data_from_yahoo_finance(start="2017-01-01"):
    """
    fetch data from yahoo finance from start date to end date, and save it to datebase
    :param start:
    :return:
    """
    conn = SqliteConnector(db_file_path)
    yahoo_finance = YahooFinanceStockDataFetcher()
    end = str(datetime.datetime.today().strftime('%Y-%m-%d'))

    for symbol in SYMBOLS:
        current_data = conn.pull_data_as_df(
            "select * from raw_stock_data where symbol='{}' and date > '2019-01-01';".format(symbol))
        if len(current_data) > 140:
            print("Data for stock {} already exists...".format(symbol))
        else:
            print("Start fetching data for stock {}...".format(symbol))
            df = yahoo_finance.get_historical_data(symbol, start, end)
            print(df.head())
            print(df.tail())
            conn.dump_df_to_sql(df, "raw_stock_data")
            time.sleep(200 + random.randint(-50, 50))
            print("End fetching data for stock {}...".format(symbol))


def main():
    conn = SqliteConnector(db_file_path)
    historical_data = fetch_daily_sp500_quotes_from_investing_com()
    save_quotes_from_investing_com_to_db(historical_data, conn)


if __name__ == "__main__":
    main()
