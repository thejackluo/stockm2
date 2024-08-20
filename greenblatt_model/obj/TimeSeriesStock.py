"""
Stock object time series for Joel Greenblatt's method

TODO: write documentations for each method
"""
import numpy as np

class TimeSeriesStock:
    # Attributes
    def __init__(self, ticker):
        self.stock_name = "TEST"
        self.ticker = ticker
        self.yearly_stock_objects = []

    # General Util
    def __str__(self):
        # Print the entire stock object
        s = f"========================================\nTIME SERIES FOR: {self.stock_name} ({self.ticker})\nSTOCK OBJECTS:\n========================================\n"
        for stock in self.yearly_stock_objects:
            s += str(stock) + "\n"
        return s

    def buy_sell(self):
        if len(self.yearly_stock_objects) != 10:
            print(f"Module does not support not 10 years of history stocks! {self.ticker}")
            return
        total_amount_invested = 0 
        fixed_profit = 0
        buy_year = 0
        buy_price = 0
        current_price = 0
        current_year = 0
        shares = 0
        THRESHOLD_SCORE = 8 #ADJUST FOR # OF STOCKS WE ARE TESTING!
        cash_on_hand = 1000

        '''
        If the relative total ranking of the stock within the year is below the THRESHOLD_SCORE, ie.
        it has a high ROIC and a high earnings yield compared to other options, and is therefore
        in the top THRESHOLD_SCORE of options available (adjust for number of stocks tested),
        we BUY the stock. If its total ranking falls above the THRESHOLD_SCORE, and we own it,
        SELL the stock.
        '''
        print("TIME SERIES BACKTEST FOR", self.yearly_stock_objects[-1].ticker)

        for stock in reversed(self.yearly_stock_objects):
            current_price = stock.current_price
            current_year = stock.year
            if shares == 0 and stock.total_rank_relative < THRESHOLD_SCORE:  # Check if it's a good buy - this ratio is probably a bit strict as the book is 20 yrs old but we see
                shares = cash_on_hand / stock.current_price
                total_amount_invested += (shares*stock.current_price)# should be teh same
                print(f"Buying {total_amount_invested} ({shares} shares of {stock.ticker} on {stock.year} at {stock.current_price})")
                buy_year = stock.year
                buy_price = stock.current_price
                #print(total_amount_invested)

            elif shares != 0 and stock.total_rank_relative > THRESHOLD_SCORE:  # Check if it's a good sell
                profit = (stock.current_price*shares - (total_amount_invested)) 

                print(f"Selling {stock.current_price*shares} ({shares} shares of {stock.ticker} on {stock.year} at {stock.current_price})")
                shares = 0
                print(f"Profit: {profit} Buy: {buy_price} Sell: {stock.current_price}, Annualised Return: {((stock.current_price/buy_price)**(1/(stock.year-buy_year)))}")
                total_amount_invested = 0
                buy_year = 0
                buy_price = 0
                cash_on_hand += profit
        if cash_on_hand > 0 and cash_on_hand != 1000:
            fixed_profit = cash_on_hand-1000
        if fixed_profit == 0 and total_amount_invested == 0:
            print(f"No Purchases Made for stock {self.yearly_stock_objects[0].ticker}")
        print(f"Final Profit: {fixed_profit}")
        if shares > 0:
            print(f"Current holdings {current_price*shares} ({shares} shares now at {current_price} from buy at {total_amount_invested}, cost basis {total_amount_invested/shares})")
            if current_year != buy_year:
                print(f"Annual return on current holdings: {((current_price/buy_price)**(1/(current_year-buy_year)))}")
        print("===========================================================================")