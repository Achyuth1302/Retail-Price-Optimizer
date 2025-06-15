from data_preparation import load_and_clean_data
from eda import run_eda
from price_elasticity import train_elasticity_model, save_model
from optimization import recommend_price

def run_pipeline():
    df = load_and_clean_data('data/cafe_sales.csv')
    print(df.head())

    run_eda(df)

    model, elasticity = train_elasticity_model(df)
    save_model(model)

    current_price = df['Price'].mean()
    suggested_price = recommend_price(elasticity, current_price)
    print(f"Suggested Optimal Price: ₹{suggested_price:.2f}")

if __name__ == "__main__":
    run_pipeline()
