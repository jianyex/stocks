import os

import pandas as pd
from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

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

class SqliteConnector(object):
    def __init__(self, db_file_path):
        DB_PATH = "sqlite:///" + db_file_path
        self.engine = create_engine(DB_PATH, echo=False)
        self.create_table()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def dump_df_to_sql(self, df):
        assert isinstance(df, pd.DataFrame)
        df.to_sql("raw_stocks_data", con=self.engine)

    def pull_data_as_df(self, query):
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
    columns = ['adj_close','close','date','high','low','open','symbol','volume']
    data = pd.read_csv(csv_data_path, header=None)
    data.columns = columns
    sql_connector = SqliteConnector(db_data_path)
    #sql_connector.dump_df_to_sql(data)
