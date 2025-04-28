# import pandas as pd
# import ta
# from vnstock import stock_historical_data
#
# # Lấy dữ liệu giá đóng cửa của mã cổ phiếu
# symbol = "VNM"
# df = stock_historical_data(symbol, "2024-01-01", "2024-03-01", "1D")
#
# # Tính MACD
# macd = ta.trend.MACD(df["close"], window_slow=26, window_fast=12, window_sign=9)
#
# # Thêm MACD vào DataFrame
# df["MACD"] = macd.macd()
# df["MACD_Signal"] = macd.macd_signal()
# df["MACD_Histogram"] = macd.macd_diff()
#
# # Hiển thị kết quả
# print(df[["time", "close", "MACD", "MACD_Signal", "MACD_Histogram"]].tail(10))

import pandas as pd
import ta
from vnstock import Vnstock
from datetime import datetime, timedelta

def macd(sock_code):
    stock = Vnstock().stock(symbol=sock_code, source='VCI')
    df = stock.quote.history(start=str(datetime.today().date() - timedelta(days=365)), end=str(datetime.today().date()), interval='1D')
    macd = ta.trend.MACD(df["close"], window_slow=26, window_fast=12, window_sign=9)
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    df["MACD_Histogram"] = macd.macd_diff()

    return df[["time", "close", "MACD", "MACD_Signal", "MACD_Histogram"]].tail(10)


# Lấy dữ liệu giá đóng cửa của mã cổ phiếu (VD: VNM - Vinamilk)
# symbol = "VNM"
# stock = Vnstock().stock(symbol='HPG', source='VCI')
# df = stock.quote.history(start=str(datetime.today().date() - timedelta(days=365)), end=str(datetime.today().date()), interval='1D')
# macd = ta.trend.MACD(df["close"], window_slow=26, window_fast=12, window_sign=9)
# df["MACD"] = macd.macd()
# df["MACD_Signal"] = macd.macd_signal()
# df["MACD_Histogram"] = macd.macd_diff()
#
# print(df[["time", "close", "MACD", "MACD_Signal", "MACD_Histogram"]].tail(10))
