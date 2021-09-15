#Bathtub Program
TOTAL_LITRES = 100
DES_TEMP = float(input("What is the desired water temperature: "))
filled_litres = 0
temp = 25

while filled_litres < TOTAL_LITRES:
    filled_litres += 1

    if temp < DES_TEMP:
        temp += 1
        print("The bath has {} litres and the water is {} degrees celsius.".format(filled_litres, temp))
    elif temp > DES_TEMP:
        temp -=1
        print("The bath has {} litres and the water is {} degrees celsius.".format(filled_litres, temp))
    else:
        print("The bath has {} litres and the water is {} degrees celsius.".format(filled_litres, temp))

if filled_litres == TOTAL_LITRES:
    print("The bath is filled and the tempertaure is {} degrees celsius".format(temp))
