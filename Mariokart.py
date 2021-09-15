#Pythons and Shells and Stars, Oh My!

def mathsCheck(starCount, shellCount):
  count = 0
  
  if starCount > shellCount:
    count = starCount - shellCount 
    return count
  elif starCount < shellCount:
    count = starCount - shellCount 
    return count
  elif starCount == shellCount:
    return 0
  else:
    return 0
  
def check():
  cleanSit = sit.strip(" ").replace(" ", "").lower()
  starCount = cleanSit.count("star")
  shellCount = cleanSit.count("shell")
  
  countUsed = mathsCheck(starCount, shellCount)
  print(mathsCheck(starCount, shellCount))
  
  if countUsed > 0:
    print("INVINCIBLLLLE!")
  elif countUsed < 0:
    print("CRASH!")
  elif countUsed == 0:
    print("Just drive.")

i = 0

while i < 1:
  sit = input("Enter: ")
  check()
