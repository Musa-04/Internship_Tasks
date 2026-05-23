cart_value = float(input("Enter cart value: "))

if cart_value >= 5000:
    discount = 20
elif cart_value >= 3000:
    discount = 10
else:
    discount = 0

print("Discount applied:", discount, "%")
