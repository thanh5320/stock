import pandas as pd
import ta
from vnstock import Vnstock
from datetime import datetime, timedelta

def rsi(sock_code, window=14, day=datetime.today().date()):
    stock = Vnstock().stock(symbol=sock_code, source='VCI')
    df = stock.quote.history(start=str(day - timedelta(days=365)), end=str(day), interval='1D')
    df["RSI_14"] = ta.momentum.RSIIndicator(df["close"], window=window).rsi()
    rsi_series = df[["time", "close", "RSI_14"]].tail(1)["RSI_14"]
    return rsi_series[rsi_series.index[0]]


# # Lấy dữ liệu giá đóng cửa của mã cổ phiếu (VD: VNM - Vinamilk)
# symbol = "VNM"
# stock = Vnstock().stock(symbol='HPG', source='VCI')
# df = stock.quote.history(start=str(datetime.today().date() - timedelta(days=365)), end=str(datetime.today().date()), interval='1D')
#
# # print(df)
#
# # Tính RSI với chu kỳ 14 ngày
# df["RSI_14"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
#
# # Hiển thị kết quả
# # print(type(df[["time", "close", "RSI_14"]].tail(1)["RSI_14"]))
# rsi_series = df[["time", "close", "RSI_14"]].tail(1)["RSI_14"]
# print(rsi_series[rsi_series.index[0]])
# # print(df[["time", "close", "RSI_14"]].tail(1)["RSI_14"][1])
