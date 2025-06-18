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
stock_codes = ['PVD', 'PVS', 'PLX' ,'SSI', 'VCI', 'HCM', 'KBC', 'TCM', 'VHC', 'SZC', 'IDC', 'VPB', 'MSN', 'VIC', 'HPG', 'TCB', 'BID', 'VHC', 'KDH', 'ACV', 'ACB', 'TNG', 'ORS', 'FPT', 'MWG', 'VPI', 'SHB', 'TPB', 'MBB', 'CTG', 'REE', 'PNJ', 'GEE', 'HDB']
# stock_codes = ['ACV']
df = pd.DataFrame(columns=['code', 'price', 'volatility'])
for stock_code in stock_codes:
  stock = Vnstock().stock(symbol=stock_code, source='VCI')
  match_price = stock.trading.price_board([stock_code]).T.loc['match', 'match_price'][0]
  ref_price = stock.trading.price_board([stock_code]).T.loc['listing', 'ref_price'][0]
  volatility = round(100 * (match_price - ref_price) / ref_price, 2)
  new_row = {'code': stock_code, 'price': match_price, 'volatility': volatility}
  df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
noti = Messenger(platform='telegram', channel='-4794328549', token_key='7201002830:AAHFVkdA-TI2uVbsnq-uxnr1QVGMi6OIEVg')
noti.send_message(message= df.to_string(), file_path=None, title='')
















