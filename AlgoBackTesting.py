import yfinance as yf
from StockInfo import StockInfo
from datetime import datetime, timedelta
from MACD import *
from RSI import *
from LineChart import *

# Chart(s)
line_chart = LineChart()

"""
INTC wth MACD & RSI
"""
INTC = StockInfo("INTC", 365)
INTC.StartToLoadData()

line_chart.NewChart(INTC.GetStockName(), ["MACD", "RSI"], 2)

# Main Stock Info Chart with MA(s)
line_chart.AddToMainChart(INTC.GetStockInfo(CONST_STOCK_CLOSE), "INTC")
MA_10 = CalSMA_StockInfo(INTC, 10)
MA_20 = CalSMA_StockInfo(INTC, 20)
MA_50 = CalSMA_StockInfo(INTC, 50)
line_chart.AddToMainChart(MA_10, "MA 10")
line_chart.AddToMainChart(MA_20, "MA 20")
line_chart.AddToMainChart(MA_50, "MA 50")

# MACD
MACD = CalMACD(INTC, 12, 26, CONST_MACD_EMA)
signal_line = CalSignalLine(MACD, 9, CONST_MACD_EMA)
signal_line_vs_MACD = CalSignalLineVsMACD(INTC, 12, 26, 9, CONST_MACD_EMA)
line_chart.AddToSubChart(MACD, 0, "MACD")
line_chart.AddToSubChart(signal_line, 0, "Signal Line")
line_chart.AddToSubChart(signal_line_vs_MACD, 0, "Signal Line vs MACD")

# RSI
RSI = CalRSI(INTC, 14, CONST_RSI_SMA)
line_chart.AddToSubChart(RSI, 1, "RSI")
line_chart.AddHorizontalLineToSubChart(30, 1)
line_chart.AddHorizontalLineToSubChart(70, 1)

line_chart.PlotChart()

"""
NFLX
"""
NFLX = StockInfo("NFLX", 365)
NFLX.StartToLoadData()

line_chart.NewChart(NFLX.GetStockName(), ["RSI-14 vs RSI-28 (SMA)", "RSI-14 vs RSI-28 (EMA)"], 2)
line_chart.AddToMainChart(NFLX.GetStockInfo(CONST_STOCK_HIGH), "HIGH")
line_chart.AddToMainChart(NFLX.GetStockInfo(CONST_STOCK_LOW), "LOW")

# RSI-14 vs RSI-28 in SMA
RSI_SMA_14 = CalRSI(INTC, 14, CONST_RSI_SMA)
RSI_SMA_28 = CalRSI(INTC, 28, CONST_RSI_SMA)
line_chart.AddToSubChart(RSI_SMA_14, 0, "RSI SMA 14")
line_chart.AddToSubChart(RSI_SMA_28, 0, "RSI SMA 28")
line_chart.AddHorizontalLineToSubChart(30, 0)
line_chart.AddHorizontalLineToSubChart(70, 0)

# RSI-14 vs RSI-28 in EMA
RSI_EMA_14 = CalRSI(INTC, 14, CONST_RSI_EMA)
RSI_EMA_28 = CalRSI(INTC, 28, CONST_RSI_EMA)
line_chart.AddToSubChart(RSI_EMA_14, 1, "RSA EMA 14")
line_chart.AddToSubChart(RSI_EMA_28, 1, "RSA EMA 28")
line_chart.AddHorizontalLineToSubChart(30, 1)
line_chart.AddHorizontalLineToSubChart(70, 1)

line_chart.PlotChart()

# Show Chart(s)
line_chart.ShowChart()





    



    

