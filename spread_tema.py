import config
import numpy as np
import alpaca_trade_api as tradeapi
from datetime import datetime, timedelta
from alpaca.trading.client import TradingClient
from alpaca.trading.stream import TradingStream
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

#Symbol traded and cooldown between consecutive trades
symbol = "AAPL"
cooldown = timedelta(seconds=0.2)

#Defining the client, stream, and api
client = TradingClient(config.API_KEY, config.API_SECRET_KEY, paper=True)
stream = tradeapi.Stream(config.API_KEY, config.API_SECRET_KEY, config.BASE_URL) 
api = tradeapi.REST(config.API_KEY, config.API_SECRET_KEY, config.BASE_URL)

#Class used to keep track of bid, ask, and spread
class Quote():
    def __init__(self):
        self.bid = 0
        self.ask = 0
        self.spread = 0
        
        self.bid_size = 0
        self.ask_size = 0
        self.last_trade_time = datetime.now()

    def update(self, data):
        if (round(data.ask_price - data.bid_price, 2) == 0.01):
            self.bid = data.bid_price
            self.ask = data.ask_price
            self.bid_size = data.bid_size
            self.ask_size = data.ask_size
            self.spread = round(data.ask_price - data.bid_price, 2)    

#Class used to keep track of the currnet positions
class Position():
    def __init__(self):
        self.total_shares = 0
        
    def update_total_shares(self, quantity, side):
        if side == 'buy':
            self.total_shares += quantity
        else:
            self.total_shares -= quantity
        print("TOTAL SHARES: ", self.total_shares)


#Function used to submit an order to the client
def submit_order(order_symbol, order_qty, order_side, order_time_in_force, data):
    if (data.size < 10): return
    quote.last_trade_time = datetime.now()
    order_details = MarketOrderRequest(symbol = order_symbol, 
                                    qty = order_qty, 
                                    side = order_side, 
                                    time_in_force = order_time_in_force)
    order = client.submit_order(order_details)
    print(order_side + " :" + data.price + "$")
    
#Function used to use triple exponential moving average 
def calculate_tema():
    historical_data = api.get_bars(symbol, "1D", limit=20).df
    ema1 = historical_data['close'].ewm(span=20, adjust=True).mean()
    ema2 = ema1.ewm(span=20, adjust=True).mean()
    ema3 = ema2.ewm(span=20, adjust=True).mean()
    tema = (3 * ema1) - (3 * ema2) + ema3
    tema = 3 * (ema1 - ema2) + ema3
    return round(tema[0], 2)

#Creating instance of quote and position
quote = Quote()
position = Position()

#Handler for quotes
async def on_quote(data):
    quote.update(data)
    
#Handler for trades
async def on_trade(data):
    if (datetime.now() - quote.last_trade_time < cooldown): return
    elif (position.total_shares < 100 and data.price == quote.ask 
        and quote.bid_size > quote.ask_size * 1.8
        and data.price > calculate_tema()):
        submit_order(symbol, 10, OrderSide.BUY, TimeInForce.DAY)
    
    elif (position.total_shares > -100 and data.price == quote.bid 
        and quote.ask_size > quote.bid_size * 1.8
        and data.price < calculate_tema()):
        submit_order(symbol, 10, OrderSide.SELL, TimeInForce.DAY)        
        
#Handler for trade updates
async def on_trade_updates(data):
    side = data.order['side']
    quantity = int(data.order['filled_qty'])
    if data.event == 'fill':
        position.update_total_shares(quantity, side)
        
#Subscribe to quotes, trades, and updates
stream.subscribe_quotes(on_quote, symbol)
stream.subscribe_trades(on_trade, symbol)
stream.subscribe_trade_updates(on_trade_updates)
#Start the stream
stream.run()
    