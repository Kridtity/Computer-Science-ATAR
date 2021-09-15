#ATAR results
while True:
    result = float(input("Enter ATAR result: "))

    if result > 80 and result <= 99.95:
        print("Congratulations!")
    elif result > 99.95:
        print("Be serious.")
    else:
        print("Bummer, eh?")
