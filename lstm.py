# load and plot dataset
from pandas import read_csv
import math
from pandas import datetime
from matplotlib import pyplot

# load dataset
series = read_csv('nyc_taxi.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)

# summarize first few rows
print(series.head())

# line plot
series.plot()
pyplot.show()

# Experiment Setup 70-30
total_records = series.size
train_end = math.floor(total_records * 0.7)
train_set = series[0:train_end]
test_set = series[train_end:]

