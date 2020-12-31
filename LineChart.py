import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datetime import date


class LineChart:

    main_data = []
    sub_data = []
    stock_name = ""
    indicator_name = ""
    
    def __init__(self, stock_name, indicator_name):
        self.main_data = []
        self.sub_data = []
        self.stock_name = stock_name
        self.indicator_name = indicator_name
        
    def AddMainData(self, data):
        self.main_data.append(data)

    def AddSubData(self, data):
        self.sub_data.append(data)
        
    def PlotChart(self):
        self.AdjData()
        fig, chart = plt.subplots(2, 1)
        chart[0].set_title(self.stock_name)
        chart[0].set_xlabel("Price")
        chart[0].set_ylabel("Date")
        
        for k in range(len(self.main_data)):
            x,y = zip(*self.main_data[k])
            chart[0].plot(x,y)
            
        chart[1].set_title(self.indicator_name)
        chart[1].set_xlabel("Value")
        chart[1].set_ylabel("Date")
        
        for k in range(len(self.sub_data)):
            x,y = zip(*self.sub_data[k])
            chart[1].plot(x,y)
            
        fig.autofmt_xdate()
        plt.show()
        
    def AdjData(self):
        start_date = date.fromisoformat('1970-01-01')
        for x in range(len(self.main_data)):
            if self.main_data[x][0][0] > start_date:
                start_date = self.main_data[x][0][0]
        for x in range(len(self.sub_data)):
            if self.sub_data[x][0][0] > start_date:
                start_date = self.sub_data[x][0][0]
                
        for x in range(len(self.main_data)):
            while True:
                if self.main_data[x][0][0] != start_date:
                    self.main_data[x].pop(0)
                else:
                    break
                if len(self.main_data[x]) == 0:
                    break
        
        for x in range(len(self.sub_data)):
            while True:
                if self.sub_data[x][0][0] != start_date:
                    self.sub_data[x].pop(0)
                else:
                    break
                if len(self.sub_data[x]) == 0:
                    break
                
            
        
            

        
            





