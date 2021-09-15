#Sum calc
print("Enter a series of numbers to be added together, pressing enter after each input. \nTo end input and display the sum, type 'end()'")
end = False

num_sum = 0
calc_input = input("Enter input here: ")

while calc_input != "end()":
    num = float(calc_input)
    num_sum = num_sum + num
    calc_input = input("Enter input here: ")

if calc_input == "end()":
    print("The sum is: " + str(num_sum))
