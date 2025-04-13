# XRP Arbitrage Trading Bot
# Samuel Horak
# March 2025

#################################################################
import data_collection as dc
#import trade_validator as tv
import time
from datetime import datetime
import trade as tr
#import log
import keyboard
import dbAccess as db
#import stats as s
import msvcrt
#from db_viz import DBVisualizer
import pytz
from colorama import Fore, Style


CAPITAL = db.get_capital()
TOTAL_PROFIT = db.get_profit()

TRADE_DIFFERENCE = 0.001 # min threshold differnce for trade to execute
FEE = 0.02 # trading fee, taking into account buying/selling 

SUCCESSFUL_TRADES = []

def main():

    global TOTAL_PROFIT
    print("------------------------------")
    print(Fore.GREEN + f"💰 Profit at open: ${TOTAL_PROFIT:.2f}" + Style.RESET_ALL)
    print(Fore.YELLOW + "Earning money", end="", flush=True)

    for _ in range(3):  
        time.sleep(0.5)
        print(".", end="", flush=True)

    print(Style.RESET_ALL + " ✅")
    print("------------------------------")
    #print(f"initial capital: {CAPITAL}")
    #print(f"initial profit: {PROFIT}")

    #iterations = 1

    start_time = time.time()
    try:
        while True:  

            # Get the current time in SAST
            tz = pytz.timezone('Africa/Johannesburg')
            current_time = datetime.now(tz).time()

            start_time = datetime.strptime("07:00:00", "%H:%M:%S").time()
            end_time = datetime.strptime("22:00:00", "%H:%M:%S").time()


            if start_time <= current_time <= end_time:
                
                # fetches orices {dict} from data_collection.py
                PRICES = dc.fetch_pricing_data()

                # Ensure the data is fetched successfully before proceeding
                if not PRICES:
                    print("No pricing data found. Retrying...")
                    time.sleep(1)  
                    continue
                
                # checks for valid trades using trade_validator.py
                trades = tr.validation(PRICES, TRADE_DIFFERENCE)

                iteration_profit = 0

                '''t = {exchange1, price1, exchange2, price2} ---> {binance, $2, kucoing, $3}'''
                for t in trades:
                    print(t)
                    if len(t) >= 4:

                        trade_profit = 0

                        # executes trade using trade.py
                        # t[1] = buy price, t[3] = sell price
                        trade_profit += tr.trade(t[1], t[3], (CAPITAL) ) # changed to $1000 per trade

                        # 2% fee subtracted from profit of each trade 
                        profit_after_fee = trade_profit * (1 - (FEE)) # FEE = 0.02

                        # adds successful trades to the list for that 'runs' summary
                        SUCCESSFUL_TRADES.append([t[0],t[1],t[2],t[3], str(profit_after_fee)])

                        # logs trades to db
                        db.log_successful_trades(t[0],t[1],t[2],t[3], str(profit_after_fee))

                        iteration_profit += profit_after_fee
                
                TOTAL_PROFIT += iteration_profit

                #iterations += 1

                # Check for keyboard interrupt to exit the loop
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key == 'q':
                        print("Exiting the loop...")
                        break

                time.sleep(1)
            else:
                print("Outside trading hours --> Exiting")
                break

    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting the loop...")

    print(db.daily_summary(SUCCESSFUL_TRADES))
    db.update_profit(TOTAL_PROFIT)

#def viz_data():
#    visualizer = DBVisualizer("trade_log.db", "trades")
#    df = visualizer.load_data()
#    visualizer.plot_all(df)

if __name__ == "__main__":

    choice = input("Enter 'r' to run the bot or 'q' to quit: ").strip().lower()
    if choice == 'v':
        #viz_data()
        main()
    elif choice == 'r':
        main()
    else:
        print("Invalid choice. Please enter 'r' to run the bot or 'q' to quit: ")
    
