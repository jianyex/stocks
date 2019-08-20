#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for daily_update.py."""

import pytest
import json

from stocks.constants import db_file_path
from stocks.sqlite_connector import SqliteConnector



from stocks.daily_update import save_quotes_from_investing_com_to_db

@pytest.fixture
def raw_json_data():
    with open(".\\investing_com_raw_data.json", "rb") as f:
        raw_json_data = json.load(f)
    return raw_json_data

@pytest.fixture
def conn():
    conn = SqliteConnector(db_file_path)
    return conn


def test_save_quotes_from_investing_com_to_db(raw_json_data, conn):
    save_quotes_from_investing_com_to_db(raw_json_data, conn)

