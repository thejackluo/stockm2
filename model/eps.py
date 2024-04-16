"""
DOCUMENTATION: eps.py

Input: Stock object
Output: An array of GOOD Stock Object and An array of REJECTED stocks (for reference)


STOCK Object (Input):
    - stock_name
    - ticker
    - current_price
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

FUNCTION
Our goal is to go through the EPS data and filter out the stocks that have below 8 years of EPS growth (simple function)
"""