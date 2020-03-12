import pandas as pd
import numpy
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches

# corona = pd.read_csv('usacoronavirus.csv')
# corona = pd.read_csv('denmarkcoronavirus.csv')
corona = pd.read_csv('chinacoronavirus.csv')
            # parse_dates=['date'],
            # delimiter = ",",
            # infer_datetime_format = True)

# Change 'date' column to a datetime value
corona['date'] = pd.to_datetime(corona.date)
# print(corona.dtypes)
print(corona)
x_date = corona['date']
y_total_cases = corona['total_cases']
y_total_deaths = corona['total_deaths']
y_new_deaths = corona['new_deaths']
y_new_cases = corona['new_cases']

#plotline + color
plt.plot(y_total_cases, color = 'green')
plt.plot(y_total_deaths, color = 'red')
plt.plot(y_new_deaths, color = 'orange')
plt.plot(y_new_cases, color = 'blue')

#title
plt.title('State of Corona')

#labels
plt.xlabel('Timeline(Days)')
plt.ylabel('Cases')
# figure out how to just print day and year


# plt.xticks(numpy.arange(corona.shape[0]), x_date, rotation=45)


#legend
green_patch = mpatches.Patch(color='green', label='Total Cases')
red_patch = mpatches.Patch(color='red', label='Total Deaths')
orange_patch = mpatches.Patch(color='orange', label='New Deaths')
blue_patch = mpatches.Patch(color='blue', label='New Cases')
plt.legend(handles=[green_patch, red_patch, orange_patch, blue_patch])

#beautify
# plt.gcf().autofmt_xdate()
plt.grid(True)

#show
plt.show()