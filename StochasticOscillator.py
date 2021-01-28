from StockInfo import StockInfo
from StockPerDateData import StockPerDateData
import math
import collections

CONST_SO_CLOSE = 0
CONST_SO_HIGH_LOW_AVG = 1

# Simple Stochastic Oscillator
def CalStochasticOscillator(stock_info, so_days, mode = CONST_SO_CLOSE):
    result = []
    data_map = stock_info.GetStockDayMapData()

    so_value = 0
    ref_value = 0
    tmp_del_low = 0
    tmp_del_high = 0
    lowest_price = 0
    highest_price = 0
    n_days_low_price = collections.deque()
    n_days_high_price = collections.deque()

    for x in range(len(data_map)):
        if len(n_days_low_price) == so_days:
            tmp_del_low = n_days_low_price[0]
            n_days_low_price.popleft()
        if len(n_days_high_price) == so_days:
            tmp_del_high = n_days_high_price[0]
            n_days_high_price.popleft()
        
        n_days_low_price.append(data_map[x][1].GetLow())
        n_days_high_price.append(data_map[x][1].GetHigh())
        
        if tmp_del_low == lowest_price:
            lowest_price = FindLowestValue(n_days_low_price)
        elif data_map[x][1].GetLow() < lowest_price:
            lowest_price = data_map[x][1].GetLow()
            
        if tmp_del_high == highest_price:
            highest_price = FindHighestValue(n_days_high_price)
        elif data_map[x][1].GetHigh() > highest_price:
            highest_price = data_map[x][1].GetHigh()
        
        #Cal SO value
        if len(n_days_low_price) == so_days and len(n_days_high_price) == so_days:
            if mode == CONST_SO_HIGH_LOW_AVG:
                ref_value = (data_map[x][1].GetHigh() + data_map[x][1].GetLow())/2
            else:
                ref_value = data_map[x][1].GetClose()
            
            so_value = (ref_value - lowest_price) / (highest_price - lowest_price) * 100
            pair = (data_map[x][0], so_value)
            result.append(pair)
        
    return result
    
def FindLowestValue(data):
    if len(data) == 0:
        return 0
    low = data[0]
    
    for x in data:
        if(x < low):
            low = x
    
    return low
    
def FindHighestValue(data):
    if len(data) == 0:
        return 0
    high = data[0]
    
    for x in data:
        if x > high:
            high = x
    
    return high
