#Author: MSHIROGANE
#Program name: BlackHat IT Password Check Cracking Tool
#Version: 1.0
#Description: Provides rough estimation of password strength by 
import itertools
import string
from datetime import datetime

def numerical_crack(code):
    attempts = 0
    start = datetime.now()
    chars = string.digits

    for x in range(min_bound, max_bound):
        for guess in itertools.product(chars, repeat = x):
            attempts += 1
            guess = ''.join(guess)
            
            if guess == code:
                time = (datetime.now()) - start
                return("Password is {}. Found in {} guesses and {} seconds.".format(code, attempts, time))

            if print_guess == True:
                print(guess)

def alphabetical_crack(code):
    attempts = 0
    start = datetime.now()
    chars = string.ascii_letters

    for x in range(min_bound, max_bound):
        for guess in itertools.product(chars, repeat = x):
            attempts += 1
            guess = ''.join(guess)

            if guess == code:
                time = (datetime.now()) - start
                return("Password is {}. Found in {} guesses and {} seconds.".format(code, attempts, time))

            if print_guess == True:
                print(guess)
                
def alphanumerical_crack(code):
    attempts = 0
    start = datetime.now()
    chars = string.ascii_letters + string.digits

    for x in range(min_bound, max_bound):
        for guess in itertools.product(chars, repeat = x):
            attempts += 1
            guess = ''.join(guess)

            if guess == code:
                time = (datetime.now()) - start
                return("Password is {}. Found in {} guesses and {} seconds.".format(code, attempts, time))

            if print_guess == True:
                print(guess)


print("BlackHat IT Password Check Cracking Tool\n\n")
mode = int(input("Enter password cracking mode:\n1. Numerical\n2. Alphabetical\n3. Alphanumerical\n\nMode: "))
password = input("Enter passcode: ")
min_bound = int(input("Enter lower bound: "))
max_bound = (int(input("Enter upper bound: ")) + 1)

print_guess = input("Print each guess (Y/N): ").upper()
if print_guess == "Y":
    print_guess = True
elif print_guess == "N":
    print_guess = False
else:
    print("Please enter a valid input.\n\n")
    
if mode == 1:
    print(numerical_crack(password))
elif mode == 2:
    print(alphabetical_crack(password))
elif mode == 3:
    print(alphanumerical_crack(password))
else:
    print("Please enter a valid input.\n\n")
           
