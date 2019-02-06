# https://python-graph-gallery.com/241-improve-area-chart/
# https://python-graph-gallery.com/area-plot/

# library
import datetime
import numpy as np
import matplotlib.pyplot as plt
'''
start = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))

for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))
'''


class sTimeProgressGraph:

    def __init__(self):
        self.expectedDay = 0  # index for Mondayss
        self.outDateFormate = '%d %b'

    def next_weekday(self, d, weekIndex):
        while(d.weekday() != self.expectedDay):
            d = d + datetime.timedelta(1)
        return d

    def changeDateFormat(self, dateStr):
        return datetime.datetime.strptime(dateStr, "%d-%m-%Y") ## '01-11-2018' 
        

    def getAllDatesBetween(self, start_date, end_date):
        from datetime import date, timedelta
        s_date = self.changeDateFormat(start_date)
        e_date = self.changeDateFormat(end_date)
        s_date = self.next_weekday(s_date, self.expectedDay)
        delta = e_date - s_date
        return [s_date + timedelta(i) for i in range(0, delta.days+1, 7)]

    def getAllFormatedDatesBetween(self, start_date, end_date):
        dates = self.getAllDatesBetween(start_date, end_date)
        return [d.strftime(self.outDateFormate) for d in dates]
        
    def showGraph(self, start_date, end_date): 
        labels = self.getAllFormatedDatesBetween(start_date, end_date)
        print('len of labels:', len(labels))
        width = len(labels)
        x = range(0, width)
        y1 = [1.5, 1.7, 2.0, 2.2, 2.0, 1.8, 2.0, 2.3, 4.5, 2.5, 4.0]
        y2 = [2.0, 1.9, 1.8, 1.9, 1.8, 1.6, 1.5, 1.3, 1.2, 1.2, 1.0]
        # Same, but add a stronger line on top (edge)
        plt.fill_between(x, y1[:width], color="skyblue", alpha=0.2)
#         plt.plot(x, y, color="Slateblue", alpha=0.6)
        plt.plot(x, y1[:width], color="green", alpha=0.6)
        plt.plot(x, y2[:width], color="red", alpha=0.6)
        plt.xticks(x, labels, rotation='45')
        plt.grid(True)
        plt.xlabel('Topic: Login')
        plt.ylabel('Progress')
        
    def showTooltip(self):
        from bokeh.io import show
        from bokeh.models import ColumnDataSource
        from bokeh.models import HoverTool
        from bokeh.palettes import Category10
        from bokeh.plotting import figure
        p2 = figure(plot_width=600, plot_height=300)
        grp_list = [1,3,5,3,5,6,7,7.5,8,5,4,6,7]
        for i in range(len(grp_list)):
             source = ColumnDataSource(
             data={'x':df.loc[df.group == grp_list[i]].x,
                   'group':df.loc[df.group == grp_list[i]].group,
                   'y':df.loc[df.group == grp_list[i]].y})
        p2.line(x='x',
                y='y',
                source=source,
                legend = grp_list[i],
                color = (Category10[3])[i])
        #add tool tips
        hover = HoverTool(tooltips =[
             ('group','@group'),('x','@x'),('y','@y')])
        p2.add_tools(hover)
        show(p2)
