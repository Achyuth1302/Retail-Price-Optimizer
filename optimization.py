def recommend_price(elasticity, current_price):
    if elasticity < -1:
        print("Product is elastic, lowering price might increase revenue.")
        return current_price * 0.9
    elif -1 <= elasticity <= 0:
        print("Product is inelastic, increasing price might increase revenue.")
        return current_price * 1.1
    else:
        print("Elasticity unclear, no recommendation.")
        return current_price
