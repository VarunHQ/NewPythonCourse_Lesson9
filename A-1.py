print(" ===== ATM Cash Dispenser ===== ")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
totalcash_dispensed = 0

serving = True
while serving:
    name = input("Enter the customer name: ")
    amount = int(input("Hello {name}! Enter the withdrawal amount: "))
    if amount <= 0: 
        print("Invaild Amount! Please enter a positive number.\n")
        continue

    print("\n Dispensing {amount} units for {name}: ")
    remaining  = amount
    idx = 1
    while idx <= 6: 
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1

        count = remaining // value
        if count > 0:
            print("{count} x {value}-unit note(s) = {count * value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            else: total_1 += count

        idx += 1


    customers_served += 1 
    totalcash_dispensed += amount

    print("Transaction complete, {name}!\n")
    again = input("Next customer? (yes/no): ").strip().lower()
    if again != "yes":
        serving = False

print("\n===== Daily Denomination Report =====")
for slot in range(1, 7):              
    if slot == 1: value, total = 100, total_100
    elif slot == 2: value, total = 50, total_50
    elif slot == 3: value, total = 20, total_20
    elif slot == 4: value, total = 10, total_10
    elif slot == 5: value, total = 5, total_5
    else: value, total = 1, total_1
    if total > 0:
        print("  {value}-unit notes dispensed : {total} ", end="")
        for note in range(total):            
            print("=", end="")
        print()

print("\nCustomers served : {customers_served}")
print("Total dispensed  : {totalcash_dispensed} units")
print("ATM session closed. Goodbye!")