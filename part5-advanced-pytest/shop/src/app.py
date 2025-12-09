def discount(price: float, user_type: str):
    discount_percent = 0.0
    if user_type == "vip":
        discount_percent = 20.0
    elif user_type == "regular":
        discount_percent = 10.0
    mult = (1 - (discount_percent / 100))
    return price * mult
