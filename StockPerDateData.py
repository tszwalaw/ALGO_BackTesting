class StockPerDateData:

    def __init__(self):
        self.high=0
        self.low=0
        self.vol=0
        self.close=0
    
    def ClearAllRecord(self):
        self.high=0
        self.low=0
        self.vol=0
        self.close=0
        
    def GetHigh(self):
        return self.high
        
    def SetHigh(self, value):
        self.high = value;
        
    def GetLow(self):
        return self.low
    
    def SetLow(self, value):
        self.low = value
        
    def GetVol(self):
        return self.vol
        
    def SetVol(self, value):
        self.vol = value
        
    def GetClose(self):
        return self.close
        
    def SetClose(self, value):
        self.close = value


        
    
