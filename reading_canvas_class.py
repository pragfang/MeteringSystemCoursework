import numpy as np

from PyQt4.QtGui import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class ReadingCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(1,1,1)
        super().__init__(self.fig)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.fig.canvas.draw()#draws the graph

    def show_bar_graph(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        for bar_number, key in enumerate(data_dict):
            self.ax.bar(bar_number,data_dict[key])
        self.ax.set_xticks(np.arange(len(data_dict))+0.4)#sets the position of each of the 'ticks' on the x-axis to center them under each bar by adding 0.4 to their positon - default bar size is 0.8
        self.ax.set_xticklabels(list(data_dict.keys()))#sets the labels of each tick to the corresponding key of the dictionary
        self.fig.autofmt_xdate()#Stops the labels overlapping along the axis
        self.ax.set_title("Total Consumption for {0}".format(date))
        self.ax.set_xlabel("Type")
        self.ax.set_ylabel("Consumption")
        self.fig.canvas.draw()#redraws the widget with the new graph data

    def show_pie_chart(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        data = list(data_dict.values())
        labels = list(data_dict.keys())
        self.ax.pie(data,labels=labels,autopct='%1.1f%%')#Creates the pie chart on the figure subplot using the given data and labels. "autopct='%1.1f%%'" formats the data values to 1 decimal place and adds the percentage symbol
        self.ax.set_title("Percentage Consumption for {0}".format(date))
        self.fig.canvas.draw()

    def show_scatter_graph(self,data,date):
        self.ax.clear()
        data_dict = dict(data)
        costs = list(data_dict.values())
        labels = list(data_dict.keys())
        self.ax.scatter(data,labels)
        self.ax.set_title("Consumption for {0}".format(date))
        self.fig.canvas.draw()

    def show_line_graph(self,data,date):
        self.ax.clear()
        data_list = []
        labels_list = []
        for Data in data:
            data_list.append(Data[0])
        for label in data:
            labels_list.append(Data[0])
        self.ax.plot(data_list,labels_list)
        self.ax.set_title("Consumption for {0}".format(date))
        self.fig.canvas.draw()
        
        
        
