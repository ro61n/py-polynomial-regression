# This program aims to help a user identify a potential upwards or downwards trend in a cryptocurrency
# The user is asked to input a pair to monitor
# The program will then get today's prices of that cryptocurrency pair from Binance's API.
# The prices are plotted on a time-series frame and a regression analysis is performed on those plots
# If at the time of using the app, there is a currency with a strong correlation to the regressed line of best fit,
# then the user can do more research into that currency pair to determine if it will make for an appropriate investment

# NB, Since this data is live and ever-changing, there may be a period where R-square is weak and the program will
# not be able to properly demonstrate polynomial regression on a specific currency pair. That, however, does not mean that
# the program does not work, it is simply the nature of the market at that point in time.

# Import modules
import requests
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Ask user to enter a currency pair
currency_pair = input("Please enter a currency pair (e.g. 'BTCUSDT', 'XRPUSDT', 'BNBUSDT' etc.): ")

# Use currency pair to get prices in the form of a list from Binance's API
currency_price = requests.get("https://api.binance.com/api/v3/klines?symbol="+currency_pair+"&interval=1d&limit=30").json()

# Declare variables to use later
x=0
x_days = []
y_prices = []

# Loop through all days in array
while x<len(currency_price):
    num_days = x #Alternative (back to front): (len(currency_price)-1)-x 
    
    # Append days and prices to respective arrays
    x_days.append([num_days])
    y_prices.append([float(currency_price[x][4])])
    x+=1 

# Training set
x_train = x_days #data for specific day
y_train = y_prices #closing price for the day

# Testing set is the same as the training set. It seems appropriate to do so.
x_test = x_days
y_test = y_prices 

# Train the Linear Regression model and plot a prediction
regressor = LinearRegression()
regressor.fit(x_train, y_train)
xx = np.linspace(0, 55, 100)
yy = regressor.predict(xx.reshape(xx.shape[0], 1))
plt.plot(xx, yy, c='g')

# Set the degree of the Polynomial Regression model
quadratic_featurizer = PolynomialFeatures(degree=2)

# This preprocessor transforms an input data matrix into a new data matrix of a given degree
x_train_quadratic = quadratic_featurizer.fit_transform(x_train)
x_test_quadratic = quadratic_featurizer.transform(x_test)

# Train and test the regressor_quadratic model
regressor_quadratic = LinearRegression()
regressor_quadratic.fit(x_train_quadratic, y_train)
xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

# Plot the graph
plt.plot(xx, regressor_quadratic.predict(xx_quadratic), c='r', linestyle='--')
plt.title(currency_pair+' price regressed on time series')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.grid(True)

plt.scatter(x_days, y_prices, marker='x', s=60)
plt.show()