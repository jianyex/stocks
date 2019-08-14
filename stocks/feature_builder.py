# -*- coding: utf-8 -*-
import pandas as pd
import os

class FeatureBuilder:
    def __init__(self, data):
        self._data = data

    def add_features(self):
        pass

    @property
    def data(self):
        return self._get_data()

    def _get_data(self):
        return self._data


if __name__ == "__main__":
    current_dir = os.getcwd()
    csv_data_path = os.path.join(current_dir, "../data/stocks.csv")
    columns = ['Adj_Close','Close','Date','High','Low','Open','Symbol','Volume']
    data = pd.read_csv(csv_data_path, header=None)
    data.columns = columns
    feature_builder = FeatureBuilder(data=data)
    print(data.head())
