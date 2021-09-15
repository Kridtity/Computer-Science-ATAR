#Comp. Sci. Discounts
#WIP
import warnings
warnings.filterwarnings("ignore", category = Warning)

while True:
    grade = input("Enter computer science grade: ").upper()
    
    try:
        grade_num = float(grade)
        print("Grade is: {}".format(grade_num))
    except:
        print("Grade is: {}".format(grade))

    if grade == "A":
        print("Discount is 25%.")
    elif grade_num >= 75 and grade_num <= 100:
        print("Discount is 25%.")
    else:
        print("Discount is 5%.")
