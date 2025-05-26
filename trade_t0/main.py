# tinh toan diem mua ban
## dua vao co phieu do
### thong tin dong cua ngay hom trc: số lượng mua bán hôm trc

# dat lenh ban
# theo doi lenh ban (tinh toan va dieu chinh)
# tinh toan lai diem mua
# dat lenh mua
# theo doi lenh mua (tinh toan va dieu chinh)
# quan tri rui ro khi cuoi ngay chua mua lai duoc co phieu da ban

from rsi import rsi
from vnstock import Vnstock

stock = Vnstock().stock(symbol='ACB', source='VCI')
stocks = stock.listing.all_symbols()
print(stocks)
stock_symbols = stocks['symbol'].tolist()

for stock_code in stock_symbols:
    try:
        t = rsi(stock_code)
        if t < 40:
          print(f'stock_code: {stock_code}, rsi={t}')
    except ValueError:
        print(f'stock_code: {stock_code} error')

