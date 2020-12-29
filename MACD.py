from MA import CalEMA, CalSMA

# Moving average convergence divergence (MACD)
def CalMACD(stock_info, fast_length, slow_length):
    
    counter_fast = 0
    counter_slow = 0
    MACD = 0
    result = []
    
    if slow_length < fast_length:
        print("MACD fast length smaller than slow length")
        return result
    EMA_fast = CalEMA(stock_info, fast_length)
    EMA_slow = CalEMA(stock_info, slow_length)
    
    while counter_slow < len(EMA_slow):
        if counter_fast >= len(EMA_fast):
            break;
            
        if EMA_fast[counter_fast][0] != EMA_slow[counter_slow][0]:
            counter_fast += 1
        else:
            MACD = EMA_fast[counter_fast][1] - EMA_slow[counter_slow][1]
            pair = (EMA_fast[counter_fast][0], MACD)
            result.append(pair)
            counter_slow += 1
            counter_fast += 1
            
    return result
