import pandas as pd
import ta
from vnstock import Vnstock
from datetime import datetime, timedelta

stock = Vnstock().stock(symbol='HPG', source='VCI')


# Dữ liệu khớp lệnh trong ngày giao dịch realtime hoặc ngày gần nhất (ngoài giờ giao dịch)
v = stock.quote.intraday(symbol='ACB', show_log=False)
print(v.to_string())

# Bước giá và khối lượng giao dịch: realtime
v= stock.quote.price_depth('ACB')
print(v)


v= stock.trading.price_board(['ACB'])
print(v.T)
