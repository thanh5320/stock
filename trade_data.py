import pandas as pd
from sqlalchemy import create_engine, text
import time
from vnstock import Quote

# Cấu hình pandas hiển thị
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

# Kết nối Postgres
engine = create_engine("postgresql+psycopg2://root:root@127.0.0.1:5432/postgres")

# Danh sách mã cổ phiếu cần lấy
symbols = ["KBC", "KDH", "DPG", "HDC", "CTG", "VPB", "VDS", "VCI", "SHS", "MSN", "DPR"]

# Khởi tạo Quote một lần cho mỗi mã
quotes = {sym: Quote(symbol=sym, source="VCI") for sym in symbols}

def insert_trade_data(df, batch_size=1000):
    insert_sql = """
    INSERT INTO public.trade_data (id, stock, price, match_type, volume, time)
    VALUES (:id, :stock, :price, :match_type, :volume, :time)
    ON CONFLICT (id, stock, time) DO NOTHING;
    """
    with engine.begin() as conn:
        for start in range(0, len(df), batch_size):
            batch = df.iloc[start:start+batch_size]
            conn.execute(text(insert_sql), batch.to_dict(orient="records"))

def fetch_data(symbol, quote):
    try:
        df = quote.intraday(page_size=15000, show_log=False)
        df["stock"] = symbol
        df["time"] = df["time"].dt.tz_convert("Asia/Ho_Chi_Minh")
        insert_trade_data(df, batch_size=1000)
        print(f"Insert completed for {symbol} (duplicates skipped).")
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu cho {symbol}: {e}")

while True:
    print("Chạy vòng lặp...")
    for sym, q in quotes.items():
        time.sleep(1)
        fetch_data(sym, q)
