#Author: MSHIROGANE
#Program Name: C5
#Version: 1.0
#Date: 09-09-2021
#Description: Program calculates the cost of purchases made by customers of an online store, including discounts.

#Try...except to handle exceptions
try:
    #Declares lists
    items_list = []
    cost_list = []

    #Prints user instructions
    print('Enter name of item, followed by price. Enter "STOP" into items prompt to cancel and display final price.\n')

    #Item input, loop until input = "STOP"
    while True:
        item = input("Enter item: ")
        if item == "STOP":
            break
        if item == "MSHIROGANE":
            print("He's gone. Reduced to atoms.")
            continue
        items_list.append(item)

        cost = float(input("Enter cost: "))
        cost_list.append(cost)

    #Asks for sale item, find in list, and apply discount
    sale_item = input("\nSale item: ")
    sale_x = items_list.index(sale_item)
    sale_cost = cost_list[sale_x]

    #Removes sale items from lists
    del items_list[sale_x]
    del cost_list[sale_x]

    #Calculates total costs of items, applies discount
    total = sum(cost_list, sale_cost)
    discounted = total * 0.9

    #Prints normal items
    print("\nNormal items:")
    for x in range(len(items_list)):
        print("{} ${:.2f}".format(items_list[x], cost_list[x]))

    #Prints sale item
    print("\nSale items:\n{} ${:.2f}".format(sale_item, sale_cost))

    #Prints gross and net totals    
    print("\nTotal: ${:.2f}\nDiscounted price: ${:.2f}".format(total, discounted))

except:
    #Error handler and message
    print("Oops, something broke.\nPlease ensure all inputs are correct.")
