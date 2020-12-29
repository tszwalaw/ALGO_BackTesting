from MA import CalEMA, CalSMA, CalEMA_Vol

# Moving average convergence divergence (MACD)
def CalMACD(stock_info, fast_length, slow_length, mode = 0):

    """
    MODE
    0: EMA
    1: SMA
    2: EMA_Vol
    """
    
    print(mode)
    counter_fast = 0
    counter_slow = 0
    MACD = 0
    result = []
    
    if slow_length < fast_length:
        print("MACD fast length smaller than slow length")
        return result
    
    MA_fast = CalMA(stock_info, fast_length, mode)
    MA_slow = CalMA(stock_info, slow_length, mode)
    
    if len(MA_fast) == 0 or len(MA_slow) == 0:
        print("MA is empty")
        return result
    
    while counter_slow < len(MA_slow):
        if counter_fast >= len(MA_fast):
            break;
            
        if MA_fast[counter_fast][0] != MA_slow[counter_slow][0]:
            counter_fast += 1
        else:
            MACD = MA_fast[counter_fast][1] - MA_slow[counter_slow][1]
            pair = (MA_fast[counter_fast][0], MACD)
            result.append(pair)
            counter_slow += 1
            counter_fast += 1

    return result
    
def CalMA(stock_info, MA_days, mode):
    if mode == 0:
        return CalEMA(stock_info, MA_days)
    if mode == 1:
        return CalSMA(stock_info, MA_days)
    if mode == 2:
        return CalEMA_Vol(stock_info, MA_days)
    
    return []
