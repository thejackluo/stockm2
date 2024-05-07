"""
DOCUMENTATION: eps.py

Input: Stock object
Output: An array of GOOD Stock Object and An array of REJECTED stocks (for reference)


STOCK Object (Input):
    - stock_name (TODO)
    - ticker
    - current_price (TODO)
    - PE
    - EPS
    - EPS_growth

STOCK Object (Output):
    - stock_name
    - ticker
    - current_price
    - PE
    - EPS
    - EPS_growth
    - Years_with_positive_EPS
    - dampener

FUNCTION
Our goal is to go through the EPS data and filter out the stocks that have below 8 years of positive EPS growth (simple function), then rank the stocks based on the highest average EPS growth over the 10 years from the good stocks. 
EPS growth for a year cannot exceed max_EPS_growth (metric)
"""

from input import all_stocks

print("=====================================")
print("P2: EPS MODULE")
print("=====================================")

# filter by years of positive growth
def filter_by_positive_growth(stocks):
    good_stocks = []
    rejected_stocks = []
    for stock in stocks:
        #print(stock.determine_num_of_negative_growths())
        if stock.determine_num_of_negative_growths() <= 2:
            good_stocks.append(stock)
        else:
            rejected_stocks.append(stock)
    return good_stocks, rejected_stocks

# rank stock with sufficient positive growth (rank stocks based on the highest average eps growth over the 10 years from the good stocks) -
# EPS growth for a year cannot exceed max_EPS_growth

def rank_by_EPS_growth(stocks):
    return sorted(stocks, key=lambda x: x.get_average_EPS_growth(x.EPS_growth), reverse=True)

good_stocks, rejected_stocks = filter_by_positive_growth(all_stocks)
ranked_stocks = rank_by_EPS_growth(good_stocks)

print("S0: GOOD STOCKS")
print("=========================")
for stock in good_stocks:
    print(stock)

print("S1: REJECTED STOCKS")
print("=========================")
for stock in rejected_stocks:
    print(stock)

print("S2: RANKED STOCKS")
print("=========================")
for stock in ranked_stocks:
    print(stock)


