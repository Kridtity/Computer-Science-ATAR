#Cheerleader

i = 0

while i < 1:
  cheer = input("Cheer: ")
  upperCheer = cheer.upper()
  n = 0
  
  for x in cheer:
    print("Give me a " + cheer[n] + ", " + cheer[n] + "!")
    n += 1
  print("What does it spell?\n" + upperCheer)
