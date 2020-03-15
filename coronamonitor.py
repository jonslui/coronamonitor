import sys
import pandas as pd
import numpy
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches

x = sys.argv[1:2]
x= ''.join(x)
print(x)
# corona = pd.read_csv('usacoronavirus.csv')
# corona = pd.read_csv('denmarkcoronavirus.csv')
corona = pd.read_csv("https://covid.ourworldindata.org/data/full_data.csv", sep = ",")
            # parse_dates=['date'],
            # delimiter = ",",
            # infer_datetime_format = True)

# Change 'date' column to a datetime value
# if (corona['location'] == "China"):
# search for something to edit the read function up top, so it only reads in certain values.
# set to true and then write all true values? -- https://datatofish.com/if-condition-in-pandas-dataframe/

corona['date'] = pd.to_datetime(corona.date)
# print(corona.dtypes)
result = (corona[corona["location"] == x])
print(result)
# if(corona[corona["location"] == "China"]):
x_date = result['date']
y_total_cases = result['total_cases']
y_total_deaths = result['total_deaths']
y_new_deaths = result['new_deaths']
y_new_cases = result['new_cases']

#plotline + color
plt.plot(y_total_cases, color = 'green')
plt.plot(y_total_deaths, color = 'red')
plt.plot(y_new_deaths, color = 'orange')
plt.plot(y_new_cases, color = 'blue')

#title
plt.title(x)

#labels
plt.xlabel('Timeline')
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
plt.gcf().autofmt_xdate()
plt.grid(True)

#show
plt.show()

