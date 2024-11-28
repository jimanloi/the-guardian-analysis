"""Your script must compute the price of a ball-point pen based on the ordered quantity.

    1-10 pieces: 0.30€
    10-25 pieces: 5% discount
    25-50 pieces: 10% discount
    50-100 pieces: 15% discount
    100+ pieces: 20% discount

    Ask user for the quantity of pen he wants to order
    Determine the effective price per pen and total price of the order
    Print the result

"""

order_quantity = int(input("Please enter the quantity of pen you would like to order : "))
original_price = 0.3
try:
    if 10 <= order_quantity <= 24:
        discounted_price = original_price*0.95
    elif 25 <= order_quantity <= 49:
        discounted_price = original_price*0.9
    elif 50 <= order_quantity <= 100:
        discounted_price = original_price*0.85
    elif order_quantity > 100:
        discounted_price = original_price*.8
    else:
        discounted_price = original_price
    total_price = discounted_price * order_quantity
    print(f"Total price for {order_quantity} is {total_price} €.")
except TypeError or ValueError:
    print("Error: Please enter a valid quantity greater than 0.")
