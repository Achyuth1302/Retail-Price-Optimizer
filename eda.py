import matplotlib.pyplot as plt
import seaborn as sns

def run_eda(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Price', y='Quantity', data=df)
    plt.title("Price vs Quantity Sold")
    plt.xlabel("Price")
    plt.ylabel("Sales Volume")
    plt.tight_layout()
    plt.show()
