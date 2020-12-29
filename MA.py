from StockInfo import StockInfo
from StockPerDateData import StockPerDateData
import math

# Simple moving average (SMA)
def CalSMA(stock_info, SMA_days):
    result = []
    
    data_map = stock_info.GetStockDayMapData()
    avg_price = 0
    
    for x in range(len(data_map)):
        if(x+1-SMA_days <= 0):
            avg_price += data_map[x][1].GetClose()
            if(x+1-SMA_days == 0):
                pair = (data_map[x][0], avg_price/SMA_days)
                result.append(pair)
        else:
            avg_price -= data_map[x-SMA_days][1].GetClose()
            avg_price += data_map[x][1].GetClose()
            
            pair = (data_map[x][0], avg_price/SMA_days)
            result.append(pair)
            
    return result
            
# Exponential moving average (EMA)
def CalEMA(stock_info, EMA_days):

    """ Smoothing value """
    smothing_constant = 2
    smoothing = smothing_constant/(1+EMA_days)
    
    result = []
    
    data_map = stock_info.GetStockDayMapData()
    avg_price = 0
    last_ema = 0
    
    for x in range(len(data_map)):
        if(x+1-EMA_days <= 0):
            avg_price += data_map[x][1].GetClose()
            if(x+1-EMA_days == 0):
                last_ema = avg_price/EMA_days
                pair = (data_map[x][0], last_ema)
                result.append(pair)
        else:
            last_ema = (data_map[x][1].GetClose()) * smoothing + (last_ema * (1 - smoothing))
            pair = (data_map[x][0], last_ema)
            result.append(pair)
        
    print(result)
    return result
    
# Exponential moving average with Volatility Changes
def CalEMA_Vol(stock_info, EMA_days):

    """ Smoothing value """
    smothing_constant = 2
    smoothing = smothing_constant/(1+EMA_days)
    
    result = []
    
    data_map = stock_info.GetStockDayMapData()
    avg_price = 0
    last_ema = 0
    
    
    for x in range(len(data_map)):
        if(x+1-EMA_days <= 0):
            avg_price += data_map[x][1].GetClose()
            if(x+1-EMA_days == 0):
                last_ema = avg_price/EMA_days
                pair = (data_map[x][0], last_ema)
                result.append(pair)
        else:
            last_ema = (data_map[x][1].GetClose()) * smoothing + (last_ema * (1 - smoothing))
            pair = (data_map[x][0], last_ema)
            result.append(pair)
        
    print(result)
    return result
