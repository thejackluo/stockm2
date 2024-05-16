"""
DOCUMENTATION: input.py

INPUT: An array of ALL tickers we want to test
OUTPUT: An array of stock objects 

STOCK OBJ:
    - ticker
    - stock_name
    - EPS_2023
    - EPS_growth (list of 10 year EPS growth)
    (other data for the future)

FUNCTION
Our goal is to go through an API and get all the data and produce ______________
"""

from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from all_stocks import all_stocks
from obj.Stock import Stock
import os
import json
import pandas as pd


# S0: Get input (US indexes Russel 1000 + 2000 V2) (S&P 500 V1)
"""
# create a list of the three test stocks (1, 5, 12) ticker only no object
# test_stocks = [all_stocks[1], all_stocks[5], all_stocks[12]] # print the first 3 stock in the all stock list as testing purposes # AAPL, GOOGL, TSLA????
"""

print("=====================================")
print("P0: Input Module")
print("=====================================") 


# S1: Add API KEY and Set Up AV SDK
load_dotenv(override=True)  # take environment variables from .env.
api_key = os.getenv('ALPHAVANTAGE_API_KEY')



if api_key:
    print("S0: API Key Success:", api_key)
    client = api_key
    #print("S0: AV SDK Client Success, current usage:", client.queries())
else:
    print("ERROR S0: Environment or API_Key variable not found.")

sample_stock = 'AAPL'
print("S1: data for stock:",  sample_stock) # Outputs the data for a sample stock

ts = TimeSeries(key = api_key,output_format = 'pandas')
data = ts.get_daily(sample_stock)
print(data[0])

######UNDER HERE COPIED FROM INPUT.PY - IT WILL CRASH AND DOES NOT WORK YET#######


# S2: For test_stocks list, RETRIEVE different attributes of the stock based on the API and initialize new stock object
# EPS Module Data V1
#resp = client.get_data_batch(companies=test_stocks, metrics=['eps_diluted_growth', 'price_to_earnings','eps_diluted','period_end_price'], period="FY-9:FY") # get 10 years eps growth, eps, pe ratio, and price for the test stocks
# Check the status of the call
print("S2: client resp number:", client.resp) # Outputs response number. If it says 207, you have content to use.
print("S2: client content:", client.resp._content) # Outputs the content of the response, if there is an error, check the error


# # # EPS Module Data V2: use the client.get_data_full to get metadata for stock and use a for loop to run through all_stocks ticker, then in each iteration, print out the data
# for ticker in test_stocks:
#     print("S2: ticker: ===================================", ticker)
#     print(client.get_data_full(symbol=ticker))



# S3: Convert json data into into PANDAS dataframe for easier manipulation
pd_stocks = json.loads(client.resp._content.decode('utf-8'))['data'] # filter and extract for the companies that you have data
pd_stocks = pd.DataFrame(pd_stocks) # transform it to a pandas dataframe
print("S3: test_stocks Pandas DataFrame", pd_stocks) # Output the dataframe to VISUALIZE the data

# S4: create stock objects for the test stocks
"""
# using numpy, get the average EPS growth for each stock, and create the stock object for each stock
# get the most recent eps growth based on teh last eps diluted growth for each stock for inputting into the stock object later\
# TODO DONE: (update stock name and current price) (currently set name to TEST, and set current price to -1)
"""


all_stocks = [] # initalize a list of stock objects

for i in range(len(test_stocks)):
    resp2 = client.get_data_full(symbol=test_stocks[i])

    stock_name = resp2.get('metadata', {}).get('name', "Unknown")
    current_price = resp2.get('financials', {}).get('ttm', {}).get('period_end_price') # TODO: price is not accurate to the day, only to the month
    ticker = test_stocks[i]
    EPS_2023 = pd_stocks.loc[ticker, 'eps_diluted'][-1]
    EPS_growth = pd_stocks.loc[ticker, 'eps_diluted_growth']
    PE = pd_stocks.loc[ticker, 'price_to_earnings']

    stock = Stock(stock_name, ticker, EPS_2023, EPS_growth, PE, current_price)
    all_stocks.append(stock)


print("S4: Stock Objects:") # Print the final stock objects based on the stringto method from all stocks
for stock in all_stocks:
    print(stock)


# S5: Output the stock objects for the next module


# ARCHIVES
"""
# Stock 1: AAPL
# AAPL = client.get_data_full(symbol='AAPL:US') 
# print(AAPL)

# client.get_data_batch(companies=test_stocks, metrics=['eps', 'roic'], period="FY-2:FY") # Example Function

# Old Current Price Retrieval
# current_price = pd_stocks.loc[ticker, 'period_end_price'][-1] #TODO - uses period end prices (believe it is year end), not the current price

"""




