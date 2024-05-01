import pandas
import matplotlib.pyplot as pyplot
import numpy as np
import seaborn

# Getting the most used data
aapl = pandas.read_csv("csvs/aapl.csv")
amzn = pandas.read_csv("csvs/amzn.csv")
csco = pandas.read_csv("csvs/csco.csv")
ford = pandas.read_csv("csvs/ford.csv")

# Cleaning some data for part 6 specifically
aapl_P6 = aapl[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
amzn_P6 = amzn[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
csco_P6 = csco[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
ford_P6 = ford[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]

def part1():
    data = pandas.read_csv("Part1_data/msft_5y.csv") #This is to take the data of the excel
    print(data.head()) #This is to show the first 4 rows of the data acquired

    data = pandas.read_csv("Part1_data/msft_5y.csv", index_col=["Date"]) #This is to define a new column for indexing
    print(data.tail()) #And this is to show the last 5 rows of the data

    data.index = pandas.to_datetime(data.index, utc=True) #This is to change the type of information from string to datetime

    data = data.asfreq("ME") #Adjust frequency to a monthly basis
    print(data.head())

    data = data.dropna() #Remove missing values from data
    print(data.head())

    percent_change = data.pct_change() #Adjust to percentages to see returning value
    percent_change = percent_change[["Open", "High", "Low", "Close"]] #Specify which columns do we want to see
    percent_change = percent_change.dropna() #Clean table
    print(percent_change.head())

    returns = percent_change.mean(axis = 1) #Get the monthly average
    print(returns.head())

    total_returns = (returns + 1).cumprod() #Get the cumulative returns
    print(total_returns.head())

    pyplot.rcParams["figure.figsize"] = (10, 5) #Set and update parameters for the future plot
    pyplot.rcParams.update({"font.size" : 12})

    pyplot.ylabel("Returns") #Add a label for the y axis

    total_returns.plot()
    pyplot.show() #Plot and show the data

def part2():

    #Obtaining the averages
    aapl_volume_average = aapl["Volume"].mean()
    amzn_volume_average = amzn["Volume"].mean()
    csco_volume_average = csco["Volume"].mean()
    ford_volume_average = ford["Volume"].mean()

    #Building the pie plot with the averages
    volume_averages = np.array([aapl_volume_average, amzn_volume_average, 
                                csco_volume_average, ford_volume_average])
    
    labels = ["Apple", "Amazon", "Cisco", "Ford"]
    pyplot.rcParams["figure.figsize"] = (10, 8)
    pyplot.pie(volume_averages, labels = labels, autopct = "%.2f")

    #Show the pie plot
    pyplot.show()

def part3():

    #Getting market capitalization
    aapl["Market cap"] = aapl["Open"] * aapl["Volume"]
    amzn["Market cap"] = amzn["Open"] * amzn["Volume"]
    csco["Market cap"] = csco["Open"] * csco["Volume"]
    ford["Market cap"] = ford["Open"] * ford["Volume"]

    #Plotting to find the lowest risk stocks
    aapl["Market cap"].plot(label = "Apple", figsize = (15, 5))
    amzn["Market cap"].plot(label = "Amazon")
    csco["Market cap"].plot(label = "Cisco")
    ford["Market cap"].plot(label = "Ford")
    
    #Showing plot
    pyplot.legend()
    pyplot.draw()
    pyplot.waitforbuttonpress(0)
    pyplot.close()

def part4():

    #Moving average for the last 50 days
    aapl["MA50"] = aapl["Close"].rolling(50).mean()
    amzn["MA50"] = amzn["Close"].rolling(50).mean()    
    csco["MA50"] = csco["Close"].rolling(50).mean()
    ford["MA50"] = ford["Close"].rolling(50).mean()

    #Moving average for the last 200 days
    aapl["MA200"] = aapl["Close"].rolling(200).mean()
    amzn["MA200"] = amzn["Close"].rolling(200).mean()
    csco["MA200"] = csco["Close"].rolling(200).mean()
    ford["MA200"] = ford["Close"].rolling(200).mean()

    #Defining plot organization
    figures, axes = pyplot.subplots(2, 2, figsize = (12, 7))

    aapl["MA50"].plot(ax = axes[0, 0])
    aapl["Close"].plot(ax = axes [0, 0])
    aapl["MA200"].plot(ax = axes[0, 0])

    amzn["MA50"].plot(ax = axes[0, 1])
    amzn["Close"].plot(ax = axes [0, 1])
    amzn["MA200"].plot(ax = axes[0, 1])

    csco["MA50"].plot(ax = axes[1, 0])
    csco["Close"].plot(ax = axes [1, 0])
    csco["MA200"].plot(ax = axes[1, 0])

    ford["MA50"].plot(ax = axes[1, 1])
    ford["Close"].plot(ax = axes [1, 1])
    ford["MA200"].plot(ax = axes[1, 1])

    #Showing plot
    pyplot.show()

def part5():

    # Gather the highs
    aapl["High"].plot(label = "Apple", figsize = (10,5))
    amzn["High"].plot(label = "Amazon")
    csco["High"].plot(label = "Cisco")
    ford["High"].plot(label = "Ford")

    pyplot.legend(loc="upper right")
    pyplot.show()

    # Gather the lows
    aapl["Low"].plot(label = "Apple", figsize = (10,5))
    amzn["Low"].plot(label = "Amazon")
    csco["Low"].plot(label = "Cisco")
    ford["Low"].plot(label = "Ford")

    pyplot.legend(loc="upper right")
    pyplot.show()

    # Gather the returns
    aapl["Returns"] = (aapl["Close"]/aapl["Close"].shift(1)) -1
    amzn["Returns"] = (amzn["Close"]/amzn["Close"].shift(1)) -1
    csco["Returns"] = (csco["Close"]/csco["Close"].shift(1)) -1
    ford["Returns"] = (ford["Close"]/ford["Close"].shift(1)) -1

    figure, axes = pyplot.subplots(2, 2, figsize = (15, 5))

    aapl["Returns"].hist(bins = 100, label = "Apple", ax = axes[0, 0])
    amzn["Returns"].hist(bins = 100, label = "Amazon", ax = axes[0, 1])
    csco["Returns"].hist(bins = 100, label = "Cisco", ax = axes[1, 0])
    ford["Returns"].hist(bins = 100, label = "Ford", ax = axes[1, 1])
    
    pyplot.show()

def part6():
    seaborn.heatmap(aapl_P6.corr(), annot = True)
    pyplot.show()

part6()