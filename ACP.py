print("===== Grocery APP =====")

low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    customer_name = input("Customer name: ")
    item_count = int(input("How many items are you buying? "))

    if item_count <= 0:
        print("Invalid item count.\n")
        continue

    customer_total = 0
    item_number = 1

    while item_number <= item_count:
        item_name = input("Item name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity.")
            continue

        item_total = price * quantity

        print(item_name + ": " + str(quantity) + " x " + str(price) + " = " + str(item_total))

        customer_total += item_total

        if price < 50:
            low_price_items += 1
        elif price <= 100:
            medium_price_items += 1
        else:
            high_price_items += 1

        item_number += 1

    customers_served += 1
    total_sales += customer_total

    print(customer_name + "'s total =", customer_total)

    next_customer = input("Next customer? (yes/no): ")

    if next_customer != "yes":
        billing = False

print("\n=== Price Band Report ===")

bands = ["Low price", "Medium price", "High price"]
counts = [low_price_items, medium_price_items, high_price_items]

for i in range(3):
    print(bands[i] + ": ", end="")
    for j in range(counts[i]):
        print("*", end="")
    print()

print("\nCustomers served:", customers_served)
print("Total sales:", total_sales)