# from vnstock import Trading
import pandas as pd
from sqlalchemy import create_engine, text
import time
#
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_colwidth", None)
# trading = Trading(source='VCI')
# x = trading.price_board(symbols_list=['MSN']).T
# print(x)

from vnstock import Quote
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
quote = Quote(symbol='KBC', source='VCI',)
df = quote.intraday(page_size= 15000, show_log=False)
# # x = quote.intraday(symbol='MSN')
# print(x)df
# engine = create_engine("postgresql+psycopg2://root:root@207.180.246.67:5432/trading_stock")
engine = create_engine("postgresql+psycopg2://root:root@127.0.0.1:5432/trading_stock")

def insert_intraday(df, batch_size=1000):
    # print("Inserting")
    insert_sql = """
    INSERT INTO tick_data (id, symbol, timestamp, price, volume)
    VALUES (:id, :stock, :time, :price, :volume)
    ON CONFLICT (id, symbol, timestamp) DO NOTHING;
    """
    with engine.begin() as conn:
        for start in range(0, len(df), batch_size):
            print("Inserting")
            batch = df.iloc[start:start+batch_size]
            conn.execute(text(insert_sql), batch.to_dict(orient="records"))

df["stock"] = "KBC"

# Chuyển time sang datetime (timezone aware -> UTC nếu cần)
# df["time"] = pd.to_datetime(df["time"])
# df["time"] = df["time"].dt.tz_convert("UTC")
df["time"] = df["time"].dt.tz_convert("Asia/Ho_Chi_Minh")

insert_intraday(df, batch_size=1000)
# print(df)

print("Insert completed (duplicates skipped).")
