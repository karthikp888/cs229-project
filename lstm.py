# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
# load dataset
series = read_csv('nyc_taxi.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# summarize first few rows
print(series.head())
# line plot
series.plot()
pyplot.show()
