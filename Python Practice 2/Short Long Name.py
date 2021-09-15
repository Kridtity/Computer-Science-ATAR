#Long/Short Names
name = input("What is your name? ")
name_length = len(name)

if name_length < 4:
    print("Hi {}, you have a short name.".format(name))
elif name_length >= 4 and name_length <= 8:
    print("Hi {}, nice to meet you.")
else:
    print("Hi {}, you have a long name.".format(name))
