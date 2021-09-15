#C1
items_list = []
cost_list = []

for x in range(3):
    item = input("Enter item: ")
    items_list.append(item)

    cost = float(input("Enter cost: "))
    cost_list.append(cost)

print("Total: ${:.2f}".format(sum(cost_list)))
