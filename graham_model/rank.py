"""
DOCUMENTATION: rank.py

Input: Stock object
Output: An array of GOOD Stock Object and An array of REJECTED stocks (for reference)


STOCK OBJ:
    - ticker
    - stock_name
    - assets
    - liabilities
    - shares
    - price

FUNCTION
Our goal is to use Graham's model to find the stocks which are undervalued
Undervalued stocks according to Graham trade at a price below their NAV (net asset value, assets-liab.),
when adjusted for the number of shares outstanding
"""

from input import all_stocks

print("=====================================")
print("P1: EPS MODULE")
print("=====================================")

# S0: Function definition
def filter_by_positive_nav(stocks): # Ignore all stocks with negative NAV
    good_stocks = []
    rejected_stocks = []
    for stock in stocks:
        if stock.net_asset_value > 0:
            good_stocks.append(stock)
        else:
            rejected_stocks.append(stock)
    return good_stocks, rejected_stocks

def rank_by_price_above_nav(stocks): # rank stock with sufficient positive growth (rank stocks based on the highest average eps growth 
# over the 10 years from the good stocks) 
    return sorted(stocks, key=lambda stock: stock.current_price_above_nav, reverse=True)

# S1: Filter the stocks by positive growth and rank the stocks
good_stocks, rejected_stocks = filter_by_positive_nav(all_stocks)
ranked_stocks = rank_by_price_above_nav(good_stocks)

# S2: Print the results

print("S1: GOOD STOCKS")
print("=========================")
for stock in good_stocks:
    print(stock)

print("S2: REJECTED STOCKS - NAV below 0")
print("=========================")
for stock in rejected_stocks:
    print(stock)

print("S3: RANKED STOCKS")
print("=========================")
for stock in ranked_stocks:
    print(stock)

# S3: See buysell.py


