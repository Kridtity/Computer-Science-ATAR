#Saving $4000 for Japan
total = 0

while total < 4000:
    savings = float(input("Enter amount saved this week: "))
    total = total + savings
    print("${} has been saved.".format(total))

print("You have saved ${}. Enjoy Japan.".format(total))
