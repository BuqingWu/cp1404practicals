number_items = int(input("Number of items: "))
total_price = 0

for i in range(1, number_items + 1):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {number_items} items is ${total_price:.2f}")