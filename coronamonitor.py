import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches

# link to WHO data
corona = pd.read_csv("https://covid.ourworldindata.org/data/full_data.csv", sep = ",")

# date to datetime for labels
corona['date'] = pd.to_datetime(corona.date)

# assigning chosen country name data to result
x = sys.argv[1:2]
x= ''.join(x)
result = (corona[corona["location"] == x])

x_date = result['date']
y_total_cases = result['total_cases']
y_total_deaths = result['total_deaths']
y_new_deaths = result['new_deaths']
y_new_cases = result['new_cases']

xi = list(range(result.shape[0] + 1))
xi.pop(0)

#plot lines + color
plt.plot(xi, y_total_cases, color = 'green')
plt.plot(xi, y_total_deaths, color = 'red')
plt.plot(xi, y_new_deaths, color = 'orange')
plt.plot(xi, y_new_cases, color = 'blue')

#title
plt.title(x)

#labels
plt.xlabel('Timeline (Days)')
plt.ylabel('Cases')

#legend
green_patch = mpatches.Patch(color='green', label='Total Cases')
red_patch = mpatches.Patch(color='red', label='Total Deaths')
orange_patch = mpatches.Patch(color='orange', label='New Deaths')
blue_patch = mpatches.Patch(color='blue', label='New Cases')
plt.legend(handles=[green_patch, red_patch, orange_patch, blue_patch])

#beautify
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False) 
plt.xticks(fontsize=14)    
plt.yticks(fontsize=14)

# plt.gcf().autofmt_xdate()
# plt.margins(0)

plt.text(0, -500, "Data source: covid.ourworldindata.org/data/full_data.csv    
       "\nAuthor: Jonathan Lui (website / @)"    
       "\nNote:"
       , fontsize=8)    

plt.grid(True)
# plt.locator_params(axis='x', numticks = len(xi) / 7)
# plt.xticks(xi)

#show
plt.show()

