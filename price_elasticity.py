from sklearn.linear_model import LinearRegression
import os
import pickle


def train_elasticity_model(df):
    X = df[['Price']]
    y = df['Quantity']

    model = LinearRegression()
    model.fit(X, y)

    # Calculate elasticity = (dQ/dP) * (P/Q)
    slope = model.coef_[0]
    avg_price = df['Price'].mean()
    avg_quantity = df['Quantity'].mean()
    elasticity = slope * (avg_price / avg_quantity)

    print(f"Price Elasticity of Demand: {elasticity:.4f}")

    return model, elasticity


def save_model(model, path='models/price_model.pkl'):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    print(f"Saving model to {path}...")  # ✅ Add this

    with open(path, 'wb') as f:
        pickle.dump(model, f)
        print(f"Model successfully saved at {path}")  # ✅ Confirmation
