import yfinance as yf
import math
from StockPerDateData import StockPerDateData
from datetime import datetime, timedelta

class StockInfo:

    """
    Input Data
    """
    stock_name = ""
    num_of_days = 0

    """
    Data List
    """
    stock_day_map_data = []

    """
    Calculate Value
    """
    stock_opening_days = 0

    ####################################################

    def __init__(self, stock_name, num_of_days):
        self.stock_name = stock_name
        self.num_of_days = num_of_days
        
    def StartToLoadData(self):
        self.stock_day_map_data = []
        self.stock_opening_days = 0
        
        data = yf.Ticker(self.stock_name)
        start_date = datetime.today() - timedelta(days=(self.num_of_days))
        end_date = datetime.today()
        hist = data.history(interval="1d", start=start_date, end=end_date)
        if hist.empty:
            return
        else:
            hist = hist.reset_index()
            for y in range(len(hist)):
                if hist['Date'][y] == "":
                    continue;
                if math.isnan(float(hist['High'][y])):
                    continue;
                if math.isnan(float(hist['Low'][y])):
                    continue;
                if math.isnan(float(hist['Volume'][y])):
                    continue;
   
                stock_per_date = StockPerDateData()
                
                stock_per_date.SetHigh(float(hist['High'][y]))
                stock_per_date.SetLow(float(hist['Low'][y]))
                stock_per_date.SetVol(float(hist['Volume'][y]))
                stock_per_date.SetClose(float(hist['Close'][y]))
                
                str_date = hist['Date'][y].strftime("%Y-%m-%d")
                pair_data = (str_date,stock_per_date)
                
                self.stock_opening_days += 1
                self.stock_day_map_data.append(pair_data)

    def GetStockDayMapData(self):
        return self.stock_day_map_data
        
            

        
        
        
    
