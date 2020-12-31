from StockInfo import *

CONST_RSI_SMA = 0
CONST_RSI_EMA = 1

def CalRSI(stock_info, RSI_days, mode = CONST_RSI_SMA):

    result = []
    data_map = stock_info.GetStockDayMapData()
    
    if mode == CONST_RSI_SMA:
        result = CalRSI_SMA(data_map, RSI_days)
        return result
    if mode == CONST_RSI_EMA:
        result = CalRSI_EMA(data_map, RSI_days)
        return result
            
    return result
    
def CalRSI_SMA(stock_data, RSI_days):
    result = []
    
    last_close = 0
    gain_avg = 0
    loss_avg = 0
    RSA = 0
    
    for x in range(len(stock_data)):
        
        if x == 0:
            last_close = stock_data[x][1].GetClose()
            continue
        if stock_data[x][1].GetClose() > last_close:
            gain_avg += (stock_data[x][1].GetClose() -  last_close) / last_close
        else:
            loss_avg += (stock_data[x][1].GetClose() -  last_close) / last_close
            
        last_close = stock_data[x][1].GetClose()
            
        if x - RSI_days > 0:
            if stock_data[x-RSI_days][1].GetClose() > stock_data[x-RSI_days-1][1].GetClose():
                gain_avg -= (stock_data[x-RSI_days][1].GetClose() -  stock_data[x-RSI_days-1][1].GetClose()) / stock_data[x-RSI_days-1][1].GetClose()
            else:
                loss_avg -= (stock_data[x-RSI_days][1].GetClose() -  stock_data[x-RSI_days-1][1].GetClose()) / stock_data[x-RSI_days-1][1].GetClose()

            RSA = 100 - (100 / (1-( (gain_avg/RSI_days)/(loss_avg/RSI_days))))
            pair = (stock_data[x][0], RSA)
            result.append(pair)

    return result
    
def CalRSI_EMA(stock_data, RSI_days):
    result = []
    
    """ Smoothing value """
    smothing_constant = 2
    smoothing = smothing_constant/(1+RSI_days)
    
    last_close = 0
    gain_avg = 0
    loss_avg = 0
    RSA = 0
    
    for x in range(len(stock_data)):
        
        if x == 0:
            last_close = stock_data[x][1].GetClose()
            continue
        if x - RSI_days <= 0:
            if stock_data[x][1].GetClose() > last_close:
                gain_avg += (stock_data[x][1].GetClose() -  last_close) / last_close
            else:
                loss_avg += (stock_data[x][1].GetClose() -  last_close) / last_close
            last_close = stock_data[x][1].GetClose()
            
            if x - RSI_days == 0:
                gain_avg / RSI_days
                loss_avg / RSI_days
                
        if x - RSI_days > 0:
            
            if stock_data[x][1].GetClose() > last_close:
                gain_avg = ((stock_data[x][1].GetClose() -  last_close) / last_close) * smoothing + gain_avg * (1 - smoothing)
            else:
                loss_avg = ((stock_data[x][1].GetClose() -  last_close) / last_close) * smoothing + loss_avg * (1 - smoothing)

            RSA = 100 - (100 / (1-( (gain_avg)/(loss_avg))))
            pair = (stock_data[x][0], RSA)
            result.append(pair)
            last_close = stock_data[x][1].GetClose()

    return result
            
        
