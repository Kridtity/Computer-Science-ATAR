#10 numbers
num_sum = 0

for x in range(10):
    num = float(input("Enter number {}: ".format(x + 1)))
    num_sum = num + num_sum

print("The sum of these 10 numbers is {}.".format(num_sum))
