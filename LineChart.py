import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datetime import date


class LineChart:
    
    def __init__(self):
        self.stock_name = []
        # Main Chart
        self.main_data = []
        self.main_chart_line_name = []
        # Sub Chart
        self.indicator_name = []
        self.sub_data = []
        self.horizontal_line = []
        self.sub_chart_line_name = []
        self.sub_chart_total = 0
        
    def NewChart(self, stock_name, indicator_name, sub_chart_total):
        self.stock_name = stock_name
        self.indicator_name = indicator_name
        self.sub_chart_total = sub_chart_total
        
        # Main Chart Reset
        self.main_data = []
        self.main_chart_line_name = []
        # Sub Chart Reset
        self.sub_data = []
        self.horizontal_line = []
        self.sub_chart_line_name = []

        for x in range(sub_chart_total):
            self.sub_data.append([])
            self.horizontal_line.append([])
            self.sub_chart_line_name.append([])
        
    def AddToMainChart(self, data, name):
        self.main_data.append(data)
        self.main_chart_line_name.append(name)

    def AddToSubChart(self, data, sub_chart_num, sub_chart_name):
        if sub_chart_num < 0 or sub_chart_num >= self.sub_chart_total:
            return
        self.sub_data[sub_chart_num].append(data)
        self.sub_chart_line_name[sub_chart_num].append(sub_chart_name)
        
    def AddHorizontalLineToSubChart(self, value, sub_chart_num):
        if sub_chart_num < 0 or sub_chart_num >= self.sub_chart_total:
            return
        self.horizontal_line[sub_chart_num].append(value)
        
    def PlotChart(self):
    
        
        self.AdjData()
        fig, chart = plt.subplots(self.sub_chart_total+1, 1)
        fig.canvas.set_window_title(self.stock_name)
        
        chart[0].set_title(self.stock_name)
        chart[0].set_xlabel("Date")
        chart[0].set_ylabel("Price")
        
        for k in range(len(self.main_data)):
            x,y = zip(*self.main_data[k])
            chart[0].plot(x, y, label = self.main_chart_line_name[k])

        chart[0].legend()
            
            
        for t in range(self.sub_chart_total):
            chart[t+1].set_title(self.indicator_name[t])
            chart[t+1].set_xlabel("Date")
            chart[t+1].set_ylabel("Value")
            
            for k in range(len(self.sub_data[t])):
                x,y = zip(*self.sub_data[t][k])
                chart[t+1].plot(x, y, label = self.sub_chart_line_name[t][k])
                
            chart[t+1].legend()
                
            if len(self.horizontal_line[t]) > 0:
                for x in self.horizontal_line[t]:
                    chart[t+1].axhline(y=x, color='r', linestyle='-.')
        
        fig.autofmt_xdate()
        
    def ShowChart(self):

        plt.show()
        
    def AdjData(self):
        start_date = date.fromisoformat('1970-01-01')
        for x in range(len(self.main_data)):
            if self.main_data[x][0][0] > start_date:
                start_date = self.main_data[x][0][0]
        for x in range(len(self.sub_data)):
            for y in range(len(self.sub_data[x])):
                if self.sub_data[x][y][0][0] > start_date:
                    start_date = self.sub_data[x][y][0][0]
                
        for x in range(len(self.main_data)):
            while True:
                if self.main_data[x][0][0] != start_date:
                    self.main_data[x].pop(0)
                else:
                    break
                if len(self.main_data[x]) == 0:
                    break
        
        for x in range(len(self.sub_data)):
            for y in range(len(self.sub_data[x])):
                while True:
                    if self.sub_data[x][y][0][0] != start_date:
                        self.sub_data[x][y].pop(0)
                    else:
                        break
                    if len(self.sub_data[x][y]) == 0:
                        break
                
            
        
            

        
            





