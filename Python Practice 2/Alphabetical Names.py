#Alphabetical Names
names_list = []

while True:
    name = input("Name: ")

    if name != "":
        names_list.append(name)
        names_list.sort()
    else:
        print(*names_list, sep = ", ")
