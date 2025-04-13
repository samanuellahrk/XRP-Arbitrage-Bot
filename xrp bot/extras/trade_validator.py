# Validates if a trade between 2 exchanges is worth it or not

######################################################

class Trade:
    def __init__(self, exchange1, price1, exchange2, price2, trade_value):
        self.exchange1 = exchange1
        self.price1 = price1
        self.exchange2 = exchange2
        self.price2 = price2
        self.trade_value = trade_value

    def __repr__(self):
        return f"Trade(exchange1={self.exchange1}, price1={self.price1}, exchange2={self.exchange2}, price2={self.price2}, trade_value={self.trade_value})"
    
def price_cacl(price1, price2):

    return((price2-price1) / price1)

def validation(PRICES, trade_diff):
    TRADING_PAIRS = []
    valid_trades_found = False
    for ex1, price1 in PRICES.items():
        for ex2, price2 in PRICES.items():
            if ex1 != ex2:  # Skip the same exchange pair
                trade_value = price_cacl(price1, price2)
                if trade_value > trade_diff:
                    TRADING_PAIRS.append([ex1, price1, ex2, price2])
                    #print(f"Trade between {ex1} and {ex2} is worth it: {trade_value}")
                    valid_trades_found = True

    # Print if no valid trades were found
    if not valid_trades_found:
        print("No valid trades were found.")

    return(TRADING_PAIRS)