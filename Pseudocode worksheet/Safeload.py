#Safeload calculator
strength = float(input("Enter strength: "))
width = float(input("Enter width: "))
depth = float(input("Enter depth: "))
length = float(input("Enter length: "))

safeload = ((strength * width * depth)/length)
print("Safeload is: " + safeload)
