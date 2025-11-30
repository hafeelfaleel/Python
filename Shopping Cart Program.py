item = input("What's the item you wish to purchase?: ")
quantity = int(input("Please enter the quantity of items: "))
price = float(input("Please enter the price of item in dollars: "))
total = price * quantity

print(f"You have bought {quantity} x {item} ")
print(f"Your total is ${total}")