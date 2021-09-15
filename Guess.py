#Guessing Game

answer = "electricity"

i = 0

while i < 1:
  userRes = input("What is my favourite food?\nGuess? ")
  lowerUserRes = userRes.lower()
  find = lowerUserRes.rfind("electricity")
  
  if find != -1:
    print("You guessed it! Buzzzz")
  else:
    print("Not even close")
