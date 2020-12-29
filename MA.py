from StockInfo import StockInfo
from StockPerDateData import StockPerDateData
import math

# Simple moving average (SMA) - stock info
def CalSMA_StockInfo(stock_info, SMA_days):

    value_list = []
    result = []
    
    data_map = stock_info.GetStockDayMapData()
    ref_price = 0
    
    for x in range(len(data_map)):
        ref_price = data_map[x][1].GetClose()
        pair = (data_map[x][0], ref_price)
        value_list.append(pair)
            
    result = CalSMA_ValueList(value_list, SMA_days)
    return result
    
# Exponential moving average (EMA) - stock info
def CalEMA_StockInfo(stock_info, EMA_days):

    value_list = []
    result = []
    data_map = stock_info.GetStockDayMapData()
    ref_price = 0
    
    for x in range(len(data_map)):
      ref_price = data_map[x][1].GetClose()
      pair = (data_map[x][0], ref_price)
      value_list.append(pair)
        
    result = CalEMA_ValueList(value_list, EMA_days)
    return result
    
# Simple moving average with Volatility Changes - stock info
def CalSMA_Vol(stock_info, SMA_days):
    result = []
    data_map = stock_info.GetStockDayMapData()
    avg_price = 0
    sum_of_vol = 0
    
    for x in range(len(data_map)):
        if x+1-SMA_days < 0:
            avg_price += (data_map[x][1].GetHigh() + data_map[x][1].GetLow())/2 * data_map[x][1].GetVol()
            sum_of_vol += data_map[x][1].GetVol()
            if x+1-SMA_days == 0:
                pair = (data_map[x][0], avg_price/sum_of_vol)
                result.append(pair)
        else:
            sum_of_vol -= data_map[x-SMA_days][1].GetVol()
            sum_of_vol += data_map[x][1].GetVol()
        
            avg_price -= (data_map[x-SMA_days][1].GetHigh() + data_map[x-SMA_days][1].GetLow())/2 * data_map[x-SMA_days][1].GetVol()
            avg_price += (data_map[x][1].GetHigh() + data_map[x][1].GetLow())/2 * data_map[x][1].GetVol()
            
            pair = (data_map[x][0], avg_price/sum_of_vol)
            result.append(pair)

    return result

#Exponential moving average with Volatility Changes - stock info
def CalEMA_Vol(stock_info, EMA_days):

    """ Smoothing value """
    smothing_constant = 2
    smoothing = smothing_constant/(1+EMA_days)
    
    result = []
    data_map = stock_info.GetStockDayMapData()
    avg_price = 0
    last_ema = 0
    sum_of_vol = 0
    current_value = 0
    
    for x in range(len(data_map)):
        if x+1-EMA_days <= 0:
            avg_price += (data_map[x][1].GetHigh() + data_map[x][1].GetLow())/2
            sum_of_vol += data_map[x][1].GetVol()
            if x+1-EMA_days == 0:
                last_ema = avg_price/EMA_days
                pair = (data_map[x][0], last_ema)
                result.append(pair)
        else:
            sum_of_vol -= data_map[x-EMA_days][1].GetVol()
            sum_of_vol += data_map[x][1].GetVol()
        
            current_value = (data_map[x][1].GetHigh() + data_map[x][1].GetLow())/2
            current_value *= data_map[x][1].GetVol() / sum_of_vol
            current_value += last_ema * (sum_of_vol-data_map[x][1].GetVol()) / sum_of_vol

            last_ema = current_value * smoothing + last_ema * (1 - smoothing)
            pair = (data_map[x][0], last_ema)
            result.append(pair)

    return result
    
# Simple moving average
def CalSMA_ValueList(value_list, SMA_days):
    result = []
    
    avg_price = 0
    
    for x in range(len(value_list)):
        if x+1-SMA_days <= 0:
            avg_price += value_list[x][1]
            if(x+1-SMA_days == 0):
                pair = (value_list[x][0], avg_price/SMA_days)
                result.append(pair)
        else:
            avg_price -= value_list[x-SMA_days][1]
            avg_price += value_list[x][1]
            
            pair = (value_list[x][0], avg_price/SMA_days)
            result.append(pair)
            
    return result
    
# Exponential moving average (EMA)
def CalEMA_ValueList(value_list, EMA_days):
    """ Smoothing value """
    smothing_constant = 2
    smoothing = smothing_constant/(1+EMA_days)

    result = []
    avg_price = 0
    last_ema = 0
    
    for x in range(len(value_list)):
        if x+1-EMA_days <= 0:
            avg_price += value_list[x][1]
            if x+1-EMA_days == 0:
                last_ema = avg_price/EMA_days
                pair = (value_list[x][0], last_ema)
                result.append(pair)
        else:
            last_ema = value_list[x][1] * smoothing + last_ema * (1 - smoothing)
            pair = (value_list[x][0], last_ema)
            result.append(pair)
    
    return result
    

