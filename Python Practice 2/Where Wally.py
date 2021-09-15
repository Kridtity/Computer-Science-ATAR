#Where's Wally?
while True:
    wally = input("Enter sentence: ").find("Wally")

    if wally == -1:
        print("Still looking...")
    else:
        print("Found him!")
