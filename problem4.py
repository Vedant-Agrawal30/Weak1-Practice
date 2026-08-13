# Problem 4: Function-Based Shopping Bill Calculator
# Write a function named:

# calculate_bill(price, quantity)
# The function must:

# Receive the product price and quantity.
# Calculate the total amount.
# Apply a 10% discount if the total is ₹2,000 or more.
# Return the total amount, discount and final amount.
# Take the product name, price and quantity from the user.

# Call the function and display:

# Product Name:
# Price:
# Quantity:
# Total Amount:
# Discount:
# Final Amount:
# Do not print the result inside the function. Return the calculated values and print them after calling the function.

print("Shopping Bill Calculator")
product_name = input("Enter the product name: ")
price = float(input("Enter the product price: "))
quantity = int(input("Enter the product quantity: "))


def calculate_bill(price, quantity):
    total = price * quantity
    discount = 0
    if total >= 2000:
        discount = total * 0.10
    final_amount = total - discount
    return total, discount, final_amount

total, discount, final_amount = calculate_bill(price, quantity)

print(f"Product Name: {product_name}")
print(f"Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total Amount: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")