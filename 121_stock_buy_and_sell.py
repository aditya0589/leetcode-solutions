prices = [7, 1, 5, 3, 6, 4]

min_price = float("inf")  # value set to +ve infinity
print("min price", min_price)
max_profit = 0

for price in prices:
    # best buying price so far
    min_price = min(min_price, price)

    # profit if we sell today
    profit = price - min_price

    # best profit so far
    max_profit = max(max_profit, profit)

print(max_profit)   # Output: 5
