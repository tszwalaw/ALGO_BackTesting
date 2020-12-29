import yfinance as yf
from StockInfo import StockInfo
from datetime import datetime, timedelta
from MACD import *

stock_name = "INTC"
checking_days = 3650

stock = StockInfo(stock_name, checking_days)
stock.StartToLoadData()

"""
Indicator
"""

MACD = CalMACD(stock, 12, 26, 3)
signal_line_vs_MACD = CalSignalLineVsMACD(stock, 12, 26, 9, CONST_EMA)

"""
ALGO
"""





    



    

