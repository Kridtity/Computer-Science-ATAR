#Bork! Bork! Bork!

i = 0

while i < 1:
  english = input("English: ")
    
  swedishChef = english.replace("i", "ee").replace("th", "z")
  last = swedishChef.rfind("!")
  swedishChef = "Swedish: " + swedishChef[:last] + ". Bork! Bork! Bork!"
  
  print(swedishChef)
