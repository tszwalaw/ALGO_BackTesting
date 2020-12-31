import yfinance as yf
import math
from StockPerDateData import StockPerDateData
from datetime import datetime, timedelta

CONST_STOCK_HIGH = 0
CONST_STOCK_LOW = 1
CONST_STOCK_CLOSE = 2
CONST_STOCK_VOL = 3

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
                
                #str_date = hist['Date'][y].strftime("%Y-%m-%d")
                pair_data = (hist['Date'][y],stock_per_date)
                
                self.stock_opening_days += 1
                self.stock_day_map_data.append(pair_data)

    def GetStockDayMapData(self):
        return self.stock_day_map_data
        
    def GetStockName(self):
        return self.stock_name
        
    def GetStockInfo(self, mode):
        result = []
        target_value = 0
        for x in range(len(self.stock_day_map_data)):
            if mode == CONST_STOCK_HIGH:
                target_value = self.stock_day_map_data[x][1].GetHigh()
            elif mode == CONST_STOCK_LOW:
                target_value = self.stock_day_map_data[x][1].GetLow()
            elif mode == CONST_STOCK_CLOSE:
                target_value = self.stock_day_map_data[x][1].GetClose()
            elif mode == CONST_STOCK_VOL:
                target_value = self.stock_day_map_data[x][1].GetVol()
            else:
                result = []
                return result
            pair = (self.stock_day_map_data[x][0], target_value)
            result.append(pair)
        return result


        
            

        
        
        
    
