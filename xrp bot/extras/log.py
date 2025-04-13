# trade logging module

##################################################

import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
DB_FILE = "trade_log.db"

def log_successful_trades(exchange1, price1, exchange2, price2, profit):
    """Logs a successful trade to the SQLite database with prices."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO trades 
                          (timestamp, exchange1, price_exchange1, exchange2, price_exchange2, profit) 
                          VALUES (datetime('now'), ?, ?, ?, ?, ?)''',
                       (exchange1, price1, exchange2, price2, profit))

        conn.commit()
        #print(f"Trade logged: {exchange1} to {exchange2}")
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
    finally:
        conn.close()  # Ensure connection is always closed
