# module to handle buying on exchange1 & selling on exchange2

#####################################################

def buy(asset_price, capital_amount):
    asset = capital_amount / asset_price  # Corrected calculation
    return asset

def sell(asset, sell_price):
    capital = asset * sell_price
    return capital

def trade(asset_buy_price, asset_sell_price, capital_amount):
    asset = buy(asset_buy_price, capital_amount)
    capital = sell(asset, asset_sell_price)
    profit = capital - capital_amount  # Corrected calculation
    return profit

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
#print(trade(2.2229, 2.2946,1000))