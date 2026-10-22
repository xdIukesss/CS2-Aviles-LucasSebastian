# Electricity Bill Calculator
RATE = 12.90
# Validate customer name 
while True: 
    name = input("Enter customer name: ")

    if name.strip() != "":
        break # Stops the loop when a valid name is entered
    else: 
        print("Invalid name, name cannot be empty")

# Validate previous reading value

while True:
    previous = float(input("Enter previous meter reading: "))

    if previous >= 0:
        break # Stops the loop when a value greater than zero is entered
    else:
        print("Invalid input, please enter a value greater than zero")

# Validate current reading value

while True:
    current = float(input("Enter current meter reading: "))

    if current >= previous:
        break # Stops the loop once a value greater than or equal to the previous reading is entered.
    else:
        print("Invalid input, please enter a value greater than or equal to the previous reading")


consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))

# Validation rules
# 1. Customer name -- Must not be empty
# 2. Previous reading -- Number at least 0
# 3. Current reading -- Number at least the previous reading
