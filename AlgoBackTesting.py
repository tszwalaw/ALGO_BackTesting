import yfinance as yf
from StockInfo import StockInfo
from datetime import datetime, timedelta
from MACD import *
from RSI import *
from LineChart import *

stock_name = "INTC"
checking_days = 3650

stock = StockInfo(stock_name, checking_days)
stock.StartToLoadData()

"""
Indicator
"""

#MACD
MACD = CalMACD(stock, 12, 26, CONST_MACD_EMA)
signal_line = CalSignalLine(MACD, 9, CONST_MACD_EMA)
signal_line_vs_MACD = CalSignalLineVsMACD(stock, 12, 26, 9, CONST_MACD_EMA)

MACD_chart = LineChart(stock.GetStockName(), "MACD")
MACD_chart.AddMainData(stock.GetStockInfo(CONST_STOCK_CLOSE))
MACD_chart.AddSubData(MACD)
MACD_chart.AddSubData(signal_line)
MACD_chart.AddSubData(signal_line_vs_MACD)
MACD_chart.PlotChart()


#RSI
RSI = CalRSI(stock, 14, CONST_RSI_SMA)
RSI_chart = LineChart(stock.GetStockName(), "RSI")
RSI_chart.AddMainData(stock.GetStockInfo(CONST_STOCK_CLOSE))
RSI_chart.AddSubData(RSI)
RSI_chart.PlotChart()

"""
ALGO
"""





    



    

