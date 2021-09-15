#C3
items_list = []
cost_list = []

print('Enter name of item, followed by price. Enter "STOP" into items prompt to cancel and display final price.')

while True:
    item = input("Enter item: ")
    if item == "STOP":
        break
    items_list.append(item)

    cost = float(input("Enter cost: "))
    cost_list.append(cost)

total = sum(cost_list)
sale = input("Sale item (y/n): ").lower()

if sale == "y":
    total = total - (total * 0.1)
    
print("Total: ${:.2f}".format(total))
