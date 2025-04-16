s, k = input().split()
topping = input().split()

# Base price table
price = {
    "S": [60, 80],
    "M": [80, 100],
    "L": [100, 120]
}

# Topping price per unit
topping_price = {
    "N": 0,
    "P": 15,
    "E": 10
}

# Ramen type index: R -> 0, T -> 1
k_index = 0 if k == "R" else 1
base = price[s][k_index]

# Check topping
if topping[0] == "N":
    total = base
else:
    t_type = topping[0]
    t_amount = int(topping[1])
    total = base + topping_price[t_type] * t_amount

print(total)
