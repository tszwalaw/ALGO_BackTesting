from MA import *

CONST_MACD_EMA = 0
CONST_MACD_SMA = 1
CONST_MACD_EMA_VOL = 2
CONST_MACD_EMA_VOL = 3

# Moving average convergence divergence (MACD)
def CalMACD(stock_info, fast_length, slow_length, mode = CONST_MACD_EMA):
    
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
    if mode == CONST_MACD_EMA:
        return CalEMA_StockInfo(stock_info, MA_days)
    if mode == CONST_MACD_SMA:
        return CalSMA_StockInfo(stock_info, MA_days)
    if mode == CONST_MACD_EMA_VOL:
        return CalEMA_Vol(stock_info, MA_days)
    if mode == CONST_MACD_SMA_VOL:
        return CalSMA_Vol(stock_info, MA_days)
    
    return []
    
# Signal vs MACD
def CalSignalLineVsMACD(stock_info, fast_length, slow_length, signal_length, mode = CONST_MACD_EMA):
    result  = []
    
    if signal_length > slow_length or signal_length > fast_length:
        print("Single line length is smaller than fast / slow length")
        return result
    
    MACD = CalMACD(stock_info, fast_length, slow_length, mode)
    if len(MACD) == 0:
        print("MACD is empty")
        return result
        
    signal_line = CalSignalLine(MACD, signal_length, mode)
    if len(signal_line) == 0:
        print("Signal line is empty)")
    
    MACD_counter = 0
    signal_line_counter= 0

    while signal_line_counter < len(signal_line):
        if MACD_counter >= len(MACD):
            break
            
        if signal_line[signal_line_counter][0] != MACD[MACD_counter][0]:
            MACD_counter += 1
            continue
            
        else:
            pair = (signal_line[signal_line_counter][0], MACD[MACD_counter][1] - signal_line[signal_line_counter][1])
            result.append(pair)
            signal_line_counter += 1
            MACD_counter += 1
            
    return result
    
def CalSignalLine(MACD, MA_days, mode):
    if mode == CONST_MACD_EMA or mode == CONST_MACD_EMA_VOL:
        return CalEMA_ValueList(MACD, MA_days)
        
    if mode == CONST_MACD_SMA or mode == CONST_MACD_SMA_VOL:
        return CalSMA_ValueList(MACD, MA_days)
    
    return []
