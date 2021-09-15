#Product calc
print("Enter a two numbers to be multiplied together, pressing enter after each input. \nTo end input and quit the program, type 'end()'")
end = False

product = 0
num1 = input("Enter the first number here: ")
if num1 == "end()":
    quit()
    
num2 = input("Enter the second number here: ")

while num1 != "end()":
    product = float(num1) * float(num2)
    print("The product is: " + str(product))
    num1 = input("Enter the first number here: ")
    if num1 == "end()":
        quit()
    
    num2 = input("Enter the second number here: ")
