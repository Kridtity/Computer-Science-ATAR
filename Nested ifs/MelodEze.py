total_spend = float(input("Enter total spent: "))

if total_spend <= 20:
    discount = 0
else:
    discount = 0.05
    if total_spend > 30 and total_spend <= 50:
        discount = 0.1
    else:
        discount = 0.15

total_cost = total_spend - (total_spend * discount)
print("Your total cost is: $" + str(total_cost))
