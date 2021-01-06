import yfinance as yf
from StockInfo import StockInfo
from datetime import datetime, timedelta
from MACD import *
from RSI import *
from LineChart import *
from ChartData import *
from SubChartInfo import *

# Chart(s)
line_chart = LineChart()

"""
INTC wth MACD & RSI
"""
INTC = StockInfo("INTC", 365)
INTC.StartToLoadData()

line_chart.NewChart(INTC.GetStockName())

line_chart.AddToMainChart("INTC-Close", INTC.GetStockInfo(CONST_STOCK_CLOSE))
line_chart.AddToMainChart("MA 10", CalSMA_StockInfo(INTC, 10))
line_chart.AddToMainChart("MA 20", CalSMA_StockInfo(INTC, 20))
line_chart.AddToMainChart("MA 30", CalSMA_StockInfo(INTC, 30))
line_chart.AddToMainChart("MA 40", CalSMA_StockInfo(INTC, 40))

# Set Sub Chart - MACD
MACD_chart = SubChartInfo("MACD")
MACD = CalMACD(INTC, 12, 26, CONST_MACD_EMA)
MACD_chart.AddChartData("MACD", MACD)
MACD_chart.AddChartData("Signal Line", CalSignalLine(MACD, 9, CONST_MACD_EMA))

line_chart.AddNewSubChartInfo(MACD_chart)

# Set Sub Chart - RSI
RSI_chart = SubChartInfo("RSI")
RSI_chart.AddChartData("RSI SMA 14", CalRSI(INTC, 14, CONST_RSI_SMA))
RSI_chart.AddHorizontalLine(30)
RSI_chart.AddHorizontalLine(70)
line_chart.AddNewSubChartInfo(RSI_chart)

line_chart.PlotChart()

"""
NFLX
"""
NFLX = StockInfo("NFLX", 365)
NFLX.StartToLoadData()

line_chart.NewChart(NFLX.GetStockName())

line_chart.AddToMainChart("NFLX-High", NFLX.GetStockInfo(CONST_STOCK_HIGH))
line_chart.AddToMainChart("NFLX-Low", NFLX.GetStockInfo(CONST_STOCK_LOW))

# Set Sub Chart - RSI SMA 14 vs 28
RSI_chart = SubChartInfo("RSI SMA 14 vs 28")
RSI_chart.AddChartData("RSI SMA 14", CalRSI(NFLX, 14, CONST_RSI_SMA))
RSI_chart.AddChartData("RSI SMA 28", CalRSI(NFLX, 28, CONST_RSI_SMA))
RSI_chart.AddHorizontalLine(30)
RSI_chart.AddHorizontalLine(70)
line_chart.AddNewSubChartInfo(RSI_chart)

# Set Sub Chart - RSI EMA 14 vs 28
RSI_chart = SubChartInfo("RSI EMA 14 vs 28")
RSI_chart.AddChartData("RSI EMA 14", CalRSI(NFLX, 14, CONST_RSI_EMA))
RSI_chart.AddChartData("RSI EMA 28", CalRSI(NFLX, 28, CONST_RSI_EMA))
RSI_chart.AddHorizontalLine(30)
RSI_chart.AddHorizontalLine(70)
line_chart.AddNewSubChartInfo(RSI_chart)

line_chart.PlotChart()

# Show Chart(s)
line_chart.ShowChart()





    



    

