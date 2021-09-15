#C2
items_list = []
cost_list = []

for x in range(3):
    item = input("Enter item: ")
    items_list.append(item)

    cost = float(input("Enter cost: "))
    cost_list.append(cost)

total = sum(cost_list)
sale = input("Sale item (y/n): ").lower()

if sale == "y":
    total = total - (total * 0.1)
    
print("Total: ${:.2f}".format(total))
