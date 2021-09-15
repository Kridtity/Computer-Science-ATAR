#Hitech Membership Discounts
while True:
    mem_level = int(input("Enter Hitech Mebership level: "))

    if mem_level == 1:
        print("You get a 5% discount.")
    elif mem_level == 2:
        print("You get a 10% discount.")
    elif mem_level == 3:
        print("You get a 15% discount.")
    elif mem_level == 4:
        print("You get a 25% discount.")
    else:
        print("You get no discount.")
