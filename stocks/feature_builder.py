# -*- coding: utf-8 -*-
import pandas as pd
import os
import talib
from stocks.sqlite_connector import SqliteConnector

class FeatureBuilder:
    def __init__(self, data):
        self._data = data

    def add_features(self):
        pass

    def add_label(self, label_def_func):
        pass

    @property
    def data(self):
        return self._get_data()

    def _get_data(self):
        return self._data


if __name__ == "__main__":
    current_dir = os.getcwd()
    db_file_path = os.path.join(current_dir, "../data/stocks.db")
    conn = SqliteConnector(db_file_path)
    query = "SELECT * FROM raw_stock_data WHERE symbol in ('AAPL', 'GILD') ORDER BY symbol, date;"
    data = conn.pull_data_as_df(query)
    feature_builder = FeatureBuilder(data=data)
    print(feature_builder.data)
