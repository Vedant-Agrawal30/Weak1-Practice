print("Electricity Bill Calculator")

name = input("Enter the customer's name: ")
consumed = float(input("Enter the number of electricity units consumed: "))

if consumed <= 100:
    electricity_charge = consumed * 2
elif consumed <= 200:
    electricity_charge = (100 * 2) + ((consumed - 100) * 3)
else:
    electricity_charge = (100 * 2) + (100 * 3) + ((consumed - 200) * 5)

surcharge = 0
if electricity_charge > 1000:
    surcharge = electricity_charge * 0.05

final_bill = electricity_charge + surcharge

print(f"Customer Name: {name}")
print(f"Units Consumed: {consumed}")
print(f"Electricity Charge: ₹{electricity_charge:.2f}")
print(f"Surcharge: ₹{surcharge:.2f}")
print(f"Final Bill: ₹{final_bill:.2f}")


    