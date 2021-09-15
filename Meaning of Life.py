#Meaning of Life?

answer = "42"
n = 1

i = 0
while i < 1:
  x = input("What is the meaning of life? ")
  
  if x != answer:
    print("Incorrect.")
    n = n + 1
  
  if x == answer:
    print("You got it in " + str(n) + " attempt(s)!")
    break
