import yfinance as yf
from StockInfo import StockInfo
from datetime import datetime, timedelta
from MACD import CalMACD

stock_name = "INTC"
checking_days = 3650

stock = StockInfo(stock_name, checking_days)
stock.StartToLoadData()

"""
Indicator
"""

MACD = CalMACD(stock, 12, 26)

"""
ALGO
"""





    



    

