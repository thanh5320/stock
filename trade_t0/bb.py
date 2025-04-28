import pandas as pd
import ta
from vnstock import Vnstock
from datetime import datetime, timedelta

stock = Vnstock().stock(symbol='HPG', source='VCI')
df = stock.quote.history(start=str(datetime.today().date() - timedelta(days=365)), end=str(datetime.today().date()), interval='1D')

df["SMA_20"] = ta.trend.SMAIndicator(df["close"], window=20).sma_indicator()
df["SMA_50"] = ta.trend.SMAIndicator(df["close"], window=50).sma_indicator()

# Hiển thị kết quả
print(df[["time", "close", "SMA_20", "SMA_50"]].tail(10))
