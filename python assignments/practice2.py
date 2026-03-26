# Task A1 — Multi-Item Shopping
name = input("Enter customer name: ")

subtotal = 0
count = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == "done":
        break

    price = float(input("Enter price: "))
    subtotal += price
    count += 1

print("Customer :", name.upper())
print("Items :", count)
print("Subtotal :", subtotal, "KZT")

# Task A2 — Tiered Discount
if subtotal < 3000:
    discount = 0
    tier = "No discount"
elif subtotal < 7000:
    discount = subtotal * 0.05
    tier = "5% discount"
else:
    discount = subtotal * 0.15
    tier = "15% discount"

total = subtotal - discount

print("-" * 30)
print("Discount tier :", tier)
print("Discount :", discount, "KZT")
print("Total :", total, "KZT")

# Task A3 — Name Analysis
print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if len(name) > 5:
    print("Long name")
else:
    print("Short name")