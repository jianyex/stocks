import os

import pandas as pd
from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class RawStockData(Base):
    __tablename__ = 'raw_stock_data'

    id = Column(Integer, primary_key=True)
    adj_close = Column(Float)
    close = Column(Float)
    date = Column(Date)
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    symbol = Column(Float)
    volume = Column(Float)

    def __init__(self, record):
        self.adj_close = record["adj_close"]
        self.close = record["close"]
        self.date = record["date"]
        self.high =  record["high"]
        self.low =  record["low"]
        self.open =  record["open"]
        self.symbol =  record["symbol"]
        self.volume = record["volume"]

class InvestingComSp500Today(Base):
    __tablename__ = 'investing_com_sp500_today'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    raw_json_data = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, record):
        self.date = record["date"]
        self.raw_json_data = record["raw_json_data"]

RELATIONS = {
    "raw_stock_data": RawStockData,
    "investing_com_sp500_today": InvestingComSp500Today
}

class SqliteConnector(object):
    def __init__(self, db_file_path):
        DB_PATH = "sqlite:///" + db_file_path
        self.engine = create_engine(DB_PATH, echo=False)
        self.create_table()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def insert_records(self, table, records):
        relation = RELATIONS[table]
        items = []
        for record in records:
            items.append(relation(record))
        try:
            self.session.add_all(items)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def dump_df_to_sql(self, df, table):
        assert isinstance(df, pd.DataFrame)
        if self.engine.dialect.has_table(self.engine, table):
            df.to_sql(table, if_exists='append', index=False, con=self.engine)
        else:
            df.to_sql(table, index=False, con=self.engine)

    def pull_data_as_df(self, query):
        assert isinstance(query, str)
        try:
            data_fetched = self.session.execute(query)
            columns = data_fetched.keys()
            df = pd.DataFrame(data_fetched.fetchall(), columns=columns)
            self.session.commit()
            return df
        except:
            self.session.rollback()
            raise

    def close_session(self):
        self.session.close()

    def start_session(self):
        self.session = self.Session()


if __name__ == "__main__":
    current_dir = os.getcwd()
    csv_data_path = os.path.join(current_dir, "../data/stocks.csv")
    db_data_path = os.path.join(current_dir, "../data/stocks.db")
    columns = ['adj_close', 'close', 'date', 'high','low', 'open','symbol', 'volume']
    data = pd.read_csv(csv_data_path, header=None)
    data.columns = columns
    sql_connector = SqliteConnector(db_data_path)
    #sql_connector.dump_df_to_sql(df=data, table="raw_stock_data")
