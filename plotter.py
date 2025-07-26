import pandas as pd
import matplotlib.pyplot as plt

def plot_price_history(product_id):
    df = pd.read_csv(f"prices/{product_id}.csv")
    plt.figure(figsize=(10, 4))
    plt.plot(pd.to_datetime(df["timestamp"]), df["price"], marker='o')
    plt.title(f"Price History for {product_id}")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"prices/{product_id}_history.png")