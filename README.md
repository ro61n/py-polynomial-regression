# Polynomial Regression - Capstone Project Lvl3T23

This program aims to help a user identify a potential upwards or downwards trend in a cryptocurrency.

The user is asked to input a pair to monitor. The program will then get today's prices of that cryptocurrency pair from Binance's API.
 
The prices are plotted on a time-series frame and a regression analysis is performed on those plots. If at the time of using the app, there is a currency with a strong correlation to the regressed line of best fit, then the user can do more research into that currency pair to determine if it will make for an appropriate investment.

NB, Since this data is live and ever-changing, there may be a period where R-square is weak and the program will not be able to properly demonstrate polynomial regression on a specific currency pair. That, however, does not mean thatthe program does not work, it is simply the nature of the market at that point in time.

Robin Titus is the maintainer and contributor of this project.

In order to run this application, you can open a command prompt, move to its directory and run 'py poly.py'.
