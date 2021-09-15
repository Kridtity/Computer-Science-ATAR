#Zoo revenue
ADULT_PRICE = 20
STUDENT_PRICE = 10
CHILD_PRICE = 5
PENSIONER_PRICE = 10

adults = int(input("Enter number of adults: "))
students = int(input("Enter number of students: "))
children = int(input("Enter number of children: "))
pensioners = int(input("Enter number of pensioners: "))

total_price = (adults * ADULT_PRICE) + (students * STUDENT_PRICE) + (children * CHILD_PRICE) + (pensioners * PENSIONER_PRICE)

print("Total revenue is: ${}".format(total_price))
