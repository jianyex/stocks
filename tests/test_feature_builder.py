#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stocks` package."""

import pytest
import os
from stocks.feature_builder import FeatureBuilder
from stocks.sqlite_connector import SqliteConnector


@pytest.fixture
def feature_builder():
    current_dir = os.getcwd()
    db_file_path = os.path.join(current_dir, "../data/stocks.db")
    conn = SqliteConnector(db_file_path)
    query = "SELECT * FROM raw_stock_data WHERE symbol in ('AAPL', 'GILD') ORDER BY symbol, date;"
    data = conn.pull_data_as_df(query)
    feature_builder = FeatureBuilder(data=data)
    return feature_builder


def test_feature_builder_data(feature_builder):
    data = feature_builder.data
    assert data.shape[0] > 2000
