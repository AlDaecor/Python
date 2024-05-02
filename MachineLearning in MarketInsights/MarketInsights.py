import pandas
import matplotlib.pyplot as pyplot
import numpy
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

path = "amzn.csv"
data = pandas.read_csv(path, index_col = ["Date"])
forecast = 30

# Limit the information to the desired piece
data = data[["Close"]]
data.columns = data.columns.str.replace("Close", "Value")

# Create a forecast
data["Prediction"] = data[["Value"]].shift(-forecast)

# Create an array based in the prediction column
x = numpy.array(data.drop(["Prediction"], axis = 1))
x = preprocessing.scale(x)
x_forecast = x[-forecast:]
x = x[:-forecast]

# Create a second array based in the prediction column
y = numpy.array(data["Prediction"])
y = y[:-forecast]

# Divide our data into training(80%) and testing(20%) groups
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

# Quickly train a linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Test the model
confidence = model.score(x_test, y_test)

# Build a prediction based on on the forecast made earlier
forecast_predicted = model.predict(x_forecast)
forecast_dates = pandas.date_range(start = "2018-03-28", end = "2018-04-26")

# Draw the prediction
pyplot.rcParams["figure.figsize"] = (15, 5)
pyplot.plot(forecast_dates, forecast_predicted)
pyplot.show()