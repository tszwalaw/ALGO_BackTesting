from datetime import datetime, timedelta
from datetime import date
from ChartData import *

class SubChartInfo:

    def __init__(self, name):
        self.name = name
        self.chart_data = []
        self.horizontal_line = []
        
    def GetName(self):
        return self.name
        
    def AddChartData(self, name, data):
        chart_data = ChartData(name, data)
        self.chart_data.append(chart_data)
        
    def GetChartData(self):
        return self.chart_data
        
    def AddHorizontalLine(self, value):
        self.horizontal_line.append(value)
        
    def GetHorizontalLine(self):
        return self.horizontal_line
        
    
        
    

