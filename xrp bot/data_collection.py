# data collection module
# collects data from multiple exchanges using ccxt

############################################
import ccxt

def fetch_pricing_data():
    prices = {}
    exchanges = []

    try:
        binance = ccxt.binance()
        exchanges.append(binance)

        kraken = ccxt.kraken()
        exchanges.append(kraken)

        bybit = ccxt.bybit()
        exchanges.append(bybit)

        coinbase = ccxt.coinbase()
        exchanges.append(coinbase)

        kucoin = ccxt.kucoin()
        exchanges.append(kucoin)

        okx = ccxt.okx()
        exchanges.append(okx)

        # Fetch current xrp/USDT price
        for exchange in exchanges:
            try:
                ticker = exchange.fetch_ticker("XRP/USDT")
                prices.update({exchange.id: ticker['last']})
            except Exception as e:
                print(f"Error fetching data from {exchange.id}: {e}")

        return(prices) # Return the prices dictionary {exchange: price}
    except Exception as e:
        print(f"Error initializing exchanges: {e}")
