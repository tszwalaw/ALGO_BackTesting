import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from datetime import date

from SubChartInfo import *


class LineChart:

    def __init__(self):
        self.stock_name = ""
        self.main_chart = []
        self.sub_chart_info = []
        
    def NewChart(self, stock_name):
        self.stock_name = stock_name
        self.main_chart = []
        self.sub_chart_info = []
        
    def AddToMainChart(self, name, data):
        chart_data = ChartData(name, data)
        self.main_chart.append(chart_data)
        
    def AddNewSubChartInfo(self, sub_chart_info):
        self.sub_chart_info.append(sub_chart_info)
        
    def PlotChart(self):
    
        self.AdjData()
            
        fig, chart = plt.subplots(len(self.sub_chart_info)+1, 1)
        fig.canvas.set_window_title(self.stock_name)
        
        # Main Chart
        chart[0].set_title(self.stock_name)
        chart[0].set_xlabel("Date")
        chart[0].set_ylabel("Price")
        
        for k in range(len(self.main_chart)):
            x,y = zip(*self.main_chart[k].GetData())
            chart[0].plot(x, y, label = self.main_chart[k].GetChartName())

        chart[0].legend()
        
        # Sub Chart(s)
        for t in range(len(self.sub_chart_info)):
            sub_chart = self.sub_chart_info[t]
            chart[t+1].set_title(sub_chart.GetName())
            chart[t+1].set_xlabel("Date")
            chart[t+1].set_ylabel("Value")
    
            for k in range(len(sub_chart.GetChartData())):
                x,y = zip(*sub_chart.GetChartData()[k].GetData())
                chart[t+1].plot(x, y, label = sub_chart.GetChartData()[k].GetChartName())

            chart[t+1].legend()
            
            if len(sub_chart.horizontal_line) > 0:
                for x in sub_chart.horizontal_line:
                    chart[t+1].axhline(y=x, color='r', linestyle='-.')
                    
        fig.autofmt_xdate()

        
    def ShowChart(self):
        plt.show()
        
    def AdjData(self):
        start_date = date.fromisoformat('1970-01-01')
        
        
        
        for x in range(len(self.main_chart)):
            if self.main_chart[x].GetData()[0][0] > start_date:
                start_date = self.main_chart[x].GetData()[0][0]
        for x in range(len(self.sub_chart_info)):
            for y in range(len(self.sub_chart_info[x].GetChartData())):
                if self.sub_chart_info[x].GetChartData()[y].GetData()[0][0] > start_date:
                    start_date = self.sub_chart_info[x].GetChartData()[y].GetData()[0][0]

        for x in range(len(self.main_chart)):
            while True:
                if self.main_chart[x].GetData()[0][0] != start_date:
                    self.main_chart[x].GetData().pop(0)
                else:
                    break
                if len(self.main_chart[x].GetData()) == 0:
                    break

        for x in range(len(self.sub_chart_info)):
            for y in range(len(self.sub_chart_info[x].GetChartData())):
                while True:
                    if self.sub_chart_info[x].GetChartData()[y].GetData()[0][0] != start_date:
                        self.sub_chart_info[x].GetChartData()[y].GetData().pop(0)
                    else:
                        break
                    if len(self.sub_chart_info[x].GetChartData()[y].GetData()) == 0:
                        break
                
            
        
            

        
            





