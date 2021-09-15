#Zoo visitor category
while True:
    category = input("Enter visitor category: ").lower()

    if category == "adult":
        print("Price is $20.")
    elif category == "student":
        print("Price is $10.")
    elif category == "child":
        print("Price is $5.")
    elif category == "pensioner":
        print("Price is $10.")
    else:
        print("Price is $20.")
