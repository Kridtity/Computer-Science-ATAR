#Aardvark!

i = 0

while i < 1:
  string = input("Enter line: ")
  lowerString = string.lower()
  aardvark = lowerString.rfind("aardvark")
  
  if aardvark != -1:
    print("Aardvark!")
  else:
    print("No aardvarks here. :(")
