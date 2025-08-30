price = float(input("Enter the original price of the product here.\n"))
discount_percent = float(input("Enter the discount percentage here.\n"))

def calculate_discount(price, discount_percent):
    discount_percent /= 100
    if discount_percent >= 0.2:
        final_price = price - (price * discount_percent)
        print(f"Your final price to pay is ${final_price}")
    else:
        print(price)

calculate_discount(price, discount_percent)