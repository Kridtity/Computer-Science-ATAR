#Duck, Duck, Goose!

i = 0

while i < 1:
  goosePos = int(input("Which number is the goose? "))

  for x in range(goosePos - 1):
    print("Duck, ")
    
  print("Goose!")
