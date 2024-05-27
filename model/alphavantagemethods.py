"""
DOCUMENTATION: alphavantagemethods.py

This is solely for usage with input.py so we can get more updated prices, despite being from the Alpha Vantage version 
"""

from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from util.all_stocks import all_stocks
from obj.Stock import Stock
import os
import json
import pandas as pd


# S0: Get input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)
"""
# create a list of the three test stocks (1, 5, 12) ticker only no object
# test_stocks = [all_stocks[1], all_stocks[5], all_stocks[12]] # print the first 3 stock in the all stock list as testing purposes # AAPL, GOOGL, TSLA????
"""
'''
print("=====================================")
print("P0: Input Module")
print("=====================================") 
'''

# S1: Add API KEY and Set Up AV SDK
load_dotenv(override=True)  # take environment variables from .env.
api_key = os.getenv('ALPHAVANTAGE_API_KEY')



if api_key:
    print("S0: API Key Success:", api_key)
    client = api_key
    #print("S0: AV SDK Client Success, current usage:", client.queries())
else:
    print("ERROR S0: Environment or API_Key variable not found.")
'''
sample_stock = 'IIPR'
print("S1: data for stock:",  sample_stock) # Outputs the data for a sample stock

ts = TimeSeries(key = api_key,output_format = 'pandas')
data = ts.get_daily(sample_stock)
print(data)

my_string = str(data)
my_string = my_string.split()
print("#######")

#print(my_string) # Output: apple, banana, cherry
latest_price = my_string[15]
print("#######")
# Extracting the top item for "close"
print('lastest price on', my_string[12], '=', latest_price) # Obtain the last closing price (to the day)
'''
#this function solely obtains the current price from alpha vantage. It is really inefficient but works for now.
def alpha_vantage_current_price_obtainer(ticker):
    stock_name = ticker
    ts = TimeSeries(key = api_key,output_format = 'pandas')
    TimeSeriesdata = ts.get_daily(stock_name) # TODO this is decently slow

    my_string = str(TimeSeriesdata)
    my_string = my_string.split() # this is really slow and not a good way to get the data from the tuple # this is actually not that slow

    latest_price = my_string[15]
    float_number = float(latest_price)
    return float_number


