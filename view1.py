# -*- coding: utf-8 -*-
"""
@author: pyoung
"""
import csv
from datetime import datetime
from bokeh.plotting import figure, output_server, show

tempdata = []
with open("data/pge_electric_billing_data_3303462706_2008-10-11_to_2015-01-15.csv","rb") as csvfile:
    tempreader = csv.reader(csvfile, delimiter=',')
    for row in tempreader:
        tempdata.append(row)
        
tempdata = tempdata[6:]
x = []
y1 = []
y2 = []
for item in tempdata:
    x.append(datetime.strptime(item[1], '%Y-%m-%d'))
    y1.append(float(item[3]))
    y2.append(item[5])
    
# output to static HTML file
output_server("kwh_by_month")
    
# Plot a `line` renderer setting the color, line thickness, title, and legend value.
p = figure(title="kWH by Month")
p.line(x, y1, legend="Temp.", x_axis_label='Month', y_axis_label='kWH')

show(p)

