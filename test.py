import pandas as pd
import numpy as np
from vnstock import Vnstock

def calculate_rsi(prices, period=14):
    """Tính RSI dựa trên giá đóng cửa."""
    delta = prices.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = pd.Series(gain).rolling(window=period, min_periods=1).mean()
    avg_loss = pd.Series(loss).rolling(window=period, min_periods=1).mean()

    rs = avg_gain / (avg_loss + 1e-10)  # Tránh chia cho 0
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Lấy danh sách mã cổ phiếu trên HOSE, HNX, UPCOM
stock1 = Vnstock().stock(symbol='ACB', source='VCI')
stocks = stock1.listing.all_symbols()
stock_symbols = stocks['ticker'].tolist()

rsi_results = []

# Duyệt qua từng mã để tính RSI
for stock2 in stock_symbols:
    # try:
    #     data = stock.quote.history(start='2025-01-01', end='2025-03-04', interval='1D')  # Dữ liệu 1 năm, theo ngày
    #     if not data.empty and 'close' in data.columns:
    #         rsi = calculate_rsi(data['close']).iloc[-1]  # Lấy RSI gần nhất
    #         rsi_results.append({'ticker': stock, 'RSI': rsi})
    # except Exception as e:
    #     print(f"Lỗi khi xử lý {stock}: {e}")
    stock = Vnstock().stock(symbol='HPG', source='VCI')
    data = stock.quote.history(start='2025-02-01', end='2025-03-04', interval='1D')  # Dữ liệu 1 năm, theo ngày
    if not data.empty and 'close' in data.columns:
        rsi = calculate_rsi(data['close']).iloc[-1]  # Lấy RSI gần nhất
        # rsi_results.append({'ticker': stock1, 'RSI': rsi})
        print({'ticker': stock2, 'RSI': rsi})

# Chuyển kết quả thành DataFrame
df_rsi = pd.DataFrame(rsi_results)
print(df_rsi.sort_values(by='RSI', ascending=True))
