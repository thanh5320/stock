class TradingBot:
    def __init__(self, orderbook_df, trade_df, volume_df):
        self.orderbook = orderbook_df
        self.trade_data = trade_df
        self.volume_data = volume_df

    def detect_buy_signal(self):
        # EMA giá
        self.trade_data['price_ema'] = self.trade_data['price'].ewm(span=5).mean()
        last_price = self.trade_data.iloc[-1]['price']
        last_ema = self.trade_data.iloc[-1]['price_ema']

        # Dòng tiền
        vol = self.volume_data
        buy_ratio = vol['acc_buy_volume'].sum() / vol['acc_volume'].sum()

        if last_price < last_ema and buy_ratio > 0.65:
            return {'action': 'BUY', 'price': last_price}
        return None

    def detect_sell_signal(self, buy_price, threshold=0.01):
        ask_price = self.orderbook['ask_1_price']
        gain = (ask_price - buy_price) / buy_price
        if gain >= threshold:
            return {'action': 'SELL', 'price': ask_price, 'gain_pct': round(gain * 100, 2)}
        return None
