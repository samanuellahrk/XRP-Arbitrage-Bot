import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class DBVisualizer:
    def __init__(self, db_file, table_name):
        self.db_file = db_file
        self.table_name = table_name

    def load_data(self):
        """Load data from the SQLite database into a Pandas DataFrame (Read-Only)."""
        conn = sqlite3.connect(f"file:{self.db_file}?mode=ro", uri=True)  # Read-Only Mode
        query = f"SELECT * FROM {self.table_name}"
        df = pd.read_sql_query(query, conn)
        conn.close()

        # Rename columns based on assumed structure
        df.columns = ["ID", "Timestamp", "Exchange1", "Price1", "Exchange2", "Price2", "Profit"]

        # Convert timestamp to datetime format
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])

        return df


    def plot_all(self, df):
        """Plot all graphs in a single figure."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 2x2 grid of plots
        fig.suptitle("Arbitrage Trading Analysis", fontsize=16)

      
        # --- Plot 1: Profit Per Trade (Last 20 Trades with Day & Month) ---
        df_last_20 = df.tail(20)  # Select the last 20 trades
        trade_indices = range(1, len(df_last_20) + 1)  # Index from 1 to 20

        # Convert timestamps to day-month format
        df_last_20["Timestamp"] = pd.to_datetime(df_last_20["Timestamp"]).dt.strftime("%d-%m")

        axes[0, 0].plot(trade_indices, df_last_20["Profit"], marker="o", linestyle="-", color="b", label="Profit")
        axes[0, 0].set_title("Profit Per Trade (Last 20 Trades)")
        axes[0, 0].set_xlabel("Trade Number")
        axes[0, 0].set_ylabel("Profit ($)")
        axes[0, 0].set_xticks(trade_indices)  # Set x-axis ticks to match indices
        axes[0, 0].set_xticklabels(df_last_20["Timestamp"], rotation=45)  # Label with day and month
        axes[0, 0].grid(True)
        axes[0, 0].legend()




        # --- Plot: Price 1 and Price 2 for the Last 20 Trades ---
        df_last_20 = df.head(20)  # Select the last 20 trades
        trade_indices = range(1, len(df_last_20) + 1)  # Index from 1 to 20

        # Convert timestamps to day-month format
        df_last_20["Timestamp"] = pd.to_datetime(df_last_20["Timestamp"]).dt.strftime("%d-%m")

        axes[0, 1].plot(trade_indices, df_last_20["Price1"], marker="o", linestyle="-", color="r", label="Price 1")
        axes[0, 1].plot(trade_indices, df_last_20["Price2"], marker="x", linestyle="--", color="g", label="Price 2")
        axes[0, 1].set_title("Buy vs Sell (Last 20 Trades)")
        axes[0, 1].set_xlabel("Trade Number")
        axes[0, 1].set_ylabel("Price ($)")
        axes[0, 1].set_xticks(trade_indices)  # Set x-axis ticks to match indices
        axes[0, 1].set_xticklabels(df_last_20["Timestamp"], rotation=45)  # Label with day and month
        axes[0, 1].grid(True)
        axes[0, 1].legend()

        # --- Plot: Average Price per Exchange (Last 20 Trades) ---
        #df_last_20 = df.tail(20)  # Select the last 20 trades

        # Group by exchange and calculate the average price for both price1 and price2
        average_prices = df.groupby("Exchange1")[["Price1"]].mean()
        

        # Plot the bar graph in the second axis
        axes[1, 0].bar(average_prices.index, average_prices["Price1"], color="r", label="Average Buy")
        #axes[1, 0].bar(average_prices.index, average_prices["Price2"], color="g", alpha=0.6, label="Average Price 2")

        # Set titles and labels
        axes[1, 0].set_title("Average Price per Exchange (Last 20 Trades)")
        axes[1, 0].set_xlabel("Exchange")
        axes[1, 0].set_ylabel("Average Price ($)")

        # Calculate the min and max of average prices
        min_price = average_prices.min().min()
        max_price = average_prices.max().max()

        # Define a y-axis limit that zooms into the range of values
        axes[1, 0].set_ylim(min_price * 0.99, max_price * 1.01)  # Zoom in on the range

        # Add legend
        axes[1, 0].legend()

        # Rotate x-axis labels if needed
        axes[1, 0].tick_params(axis="x", rotation=45)

        # Display grid
        axes[1, 0].grid(True)


        # --- Plot 4: Profit Distribution Histogram ---
        axes[1, 1].hist(df["Profit"], bins=10, color="green", edgecolor="black", alpha=0.7)
        axes[1, 1].set_title("Distribution of Arbitrage Profits")
        axes[1, 1].set_xlabel("Profit ($)")
        axes[1, 1].set_ylabel("Frequency")
        axes[1, 1].grid(axis="y")

        # Adjust layout for better spacing
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()
