print("================================")
print("  ELECTRICITY BILL MANAGEMENT")
print("================================")

# Customer Details
name = input("Enter Customer Name: ")
customer_id = input("Enter Customer ID: ")

# Appliance Details
appliances = []
total_units = 0

n = int(input("\nEnter number of appliances: "))

for i in range(n):

    print("\nAppliance", i + 1)

    appliance_name = input("Enter appliance name: ")
    watt = float(input("Enter power in watts: "))
    quantity = int(input("Enter quantity: "))
    hours = float(input("Enter daily usage hours: "))

    # Monthly Unit Calculation
    units = (watt * quantity * hours * 30) / 1000

    total_units += units

    appliances.append({
        "name": appliance_name,
        "units": units
    })

# Slab-wise Bill Calculation
if total_units <= 50:
    bill = total_units * 3

elif total_units <= 100:
    bill = (50 * 3) + (total_units - 50) * 5

else:
    bill = (50 * 3) + (50 * 5) + (total_units - 100) * 7

# Fixed Charges
fixed_charge = 50
total_bill = bill + fixed_charge

# Final Bill
print("\n========== MONTHLY BILL ==========")

print("Customer Name:", name)
print("Customer ID:", customer_id)

print("\nAppliance-wise Consumption:")

for appliance in appliances:
    print(appliance["name"], ":", round(appliance["units"], 2), "units")

print("\nTotal Units:", round(total_units, 2))
print("Energy Charges: Rs.", round(bill, 2))
print("Fixed Charges: Rs.", fixed_charge)
print("Final Electricity Bill: Rs.", round(total_bill, 2))

print("==================================")




