from vnstock import Vnstock
from vnstock.botbuilder.noti import Messenger
import pandas as pd

# stock_code = 'TCB'
# stock = Vnstock().stock(symbol=stock_code, source='VCI')
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
# ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
# volatility = round(100 * (match_price - ref_price) / ref_price, 2)
# noti.send_message(message= f'{stock_code}  {match_price} {volatility}', file_path=None, title='')
# stock_code = 'REE'
# stock = Vnstock().stock(symbol=stock_code, source='VCI')
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
# ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
# volatility = round(100 * (match_price - ref_price) / ref_price, 2)
# noti.send_message(message= f'{stock_code}  {match_price} {volatility}', file_path=None, title='')
# stock_code = 'CTG'
# stock = Vnstock().stock(symbol=stock_code, source='VCI')
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
# ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
# volatility = round(100 * (match_price - ref_price) / ref_price, 2)
# noti.send_message(message= f'{stock_code}  {match_price} {volatility}', file_path=None, title='')
# stock_code = 'BID'
# stock = Vnstock().stock(symbol=stock_code, source='VCI')
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
# ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
# volatility = round(100 * (match_price - ref_price) / ref_price, 2)
# noti.send_message(message= f'{stock_code}  {match_price} {volatility}', file_path=None, title='')
# stock_code = 'ACV'
# stock = Vnstock().stock(symbol=stock_code, source='VCI')
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
# ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
# volatility = round(100 * (match_price - ref_price) / ref_price, 2)
# noti.send_message(message= f'{stock_code}  {match_price} {volatility}', file_path=None, title='')
#
#
#
#
#
#
# stock_codes = ['CTG', 'TCB', 'ACV', 'FPT', 'BID', 'HPG', 'TPB', 'ORS', 'KDH', 'TNG', 'VNI']
# stock_codes = ['CAP', 'MSN', 'VIC', 'HPG', 'TCB', 'BID', 'VHC', 'KDH', 'KSB', 'ACV', 'ACB', 'TNG', 'ORS', 'FPT', 'MWG', 'VPI', 'VJC', 'SHS', 'SHB', 'TPB', 'MBB', 'CTG', 'REE', 'PNJ']
# # stock_codes = ['ACV', 'CAP']
# df = pd.DataFrame(columns=['code', 'price', 'volatility'])
# for stock_code in stock_codes:
#   stock = Vnstock().stock(symbol=stock_code, source='VCI')
#   match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
#   ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
#   volatility = round(100 * (match_price - ref_price) / ref_price, 2)
#   new_row = {'code': stock_code, 'price': match_price, 'volatility': volatility}
#   df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
# noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
# noti.send_message(message= df.to_string(), file_path=None, title='')

# stock = Vnstock().stock(symbol='CAP', source='VCI')
# lich su giao dich
# df = stock.quote.intraday(symbol='CAP', page_size=10_000, show_log=False)
# print(df)

#Bước giá và khối lượng giao dịch: realtime
# df = stock.quote.price_depth('CAP')
# print(df)

#
# df = stock.trading.price_board(['CAP']).T
# pd.set_option('display.max_rows', None)
# print(df)

stock = Vnstock().stock(symbol='CAP', source='VCI')
trade_df = stock.quote.intraday(symbol='CAP', page_size=10_000, show_log=False)
print(df)

df = stock.quote.price_depth('CAP')
print(df)


orderbook_df = stock.trading.price_board(['CAP']).T
# pd.set_option('display.max_rows', None)
# print(df)

bot = TradingBot(orderbook_df, trade_df, volume_df)

while True:
    buy_signal = bot.detect_buy_signal()
    if buy_signal:
        print("Mua vào:", buy_signal)
        # giả sử đã mua, theo dõi để bán
        for _ in range(60):
            sell_signal = bot.detect_sell_signal(buy_price=buy_signal['price'])
            if sell_signal:
                print("Bán ra:", sell_signal)
                break
            time.sleep(2)
















