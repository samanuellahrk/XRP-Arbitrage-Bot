# fetches info from DB, and provides summarised stats

############################################################
import sqlite3
from colorama import Fore, Style

DB_FILE = "trade_log.db"

def get_top_trade():
    """Fetches most profitable trade."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trades ORDER BY profit DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return (f"---------------------------------\nTrade ID: {result[0]} ({result[1]})\n{result[2]} (${result[3]}) -> {result[4]} (${result[5]})\nProfit: ${result[6]:.2f}\n---------------------------------")  # Return None if no data found

def get_worst_trade():
    """Fetches most profitable trade."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trades ORDER BY profit ASC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return (f"---------------------------------\nTrade ID: {result[0]} ({result[1]})\n{result[2]} (${result[3]}) -> {result[4]} (${result[5]})\nProfit: ${result[6]:.2f}\n---------------------------------")  # Return None if no data found

# trades [ [ ex1, price1, ex2, price2, profit ] ]
# total profit
# most profitable trade
# least profitable trade
# number of trades
# average profit per trade
def daily_summary(trades):
    """Provides a daily summary of trades."""
    if not trades:
        return (Fore.RED + "No summary available." + Style.RESET_ALL)

    total_profit = sum(float(trade[4]) for trade in trades)
    trade_count = len(trades)
    average_profit = total_profit / trade_count if trade_count > 0 else 0

    most_profitable_trade = max(trades, key=lambda x: float(x[4]))
    least_profitable_trade = min(trades, key=lambda x: float(x[4]))

    summary = (
        f"{Fore.CYAN}📊 DAILY SUMMARY 📊{Style.RESET_ALL}\n"
        f"{Fore.MAGENTA}{'=' * 35}{Style.RESET_ALL}\n"
        f"💰 Total Profit: {Fore.GREEN}${total_profit:.2f}{Style.RESET_ALL}\n"
        f"📈 Number of Trades: {Fore.YELLOW}{trade_count}{Style.RESET_ALL}\n"
        f"📊 Avg Profit per Trade: {Fore.BLUE}${average_profit:.2f}{Style.RESET_ALL}\n"
        f"{Fore.MAGENTA}{'=' * 35}{Style.RESET_ALL}\n"
        f"🔥 {Fore.LIGHTGREEN_EX}Most Profitable Trade:{Style.RESET_ALL}\n"
        f"🏦 Exchange 1: {Fore.YELLOW}{most_profitable_trade[0]}{Style.RESET_ALL}, Price 1: ${most_profitable_trade[1]:.2f}\n"
        f"🏦 Exchange 2: {Fore.YELLOW}{most_profitable_trade[2]}{Style.RESET_ALL}, Price 2: ${most_profitable_trade[3]:.2f}\n"
        f"💵 Profit: {Fore.GREEN}${float(most_profitable_trade[4]):.2f}{Style.RESET_ALL}\n"
        f"{Fore.MAGENTA}{'-' * 35}{Style.RESET_ALL}\n"
        f"📉 {Fore.LIGHTRED_EX}Least Profitable Trade:{Style.RESET_ALL}\n"
        f"🏦 Exchange 1: {Fore.YELLOW}{least_profitable_trade[0]}{Style.RESET_ALL}, Price 1: ${least_profitable_trade[1]:.2f}\n"
        f"🏦 Exchange 2: {Fore.YELLOW}{least_profitable_trade[2]}{Style.RESET_ALL}, Price 2: ${least_profitable_trade[3]:.2f}\n"
        f"💵 Profit: {Fore.RED}${float(least_profitable_trade[4]):.2f}{Style.RESET_ALL}\n"
        f"{Fore.MAGENTA}{'=' * 35}{Style.RESET_ALL}"
    )
    return summary
    

