#Author: Kridtity Ikhlaas Lawang
#Program name: BlackHat IT On-site Computer Repair Calculation Program
#Version: 0.0
#Description: Program calculates costs for an on-site BlackHat IT computer repair based on hours taken and distance travelled

while True:
    try:
        #Prints intro
        print("BlackHat IT: On-site Computer Repair Calculation Program\n")
        
        #Declares variables and assigns values
        CALLOUT_FEE = 50
        PER_HOUR = 50
        PER_KM = 3.5

        job_number = input("Enter job number: ")
        hours = float(input("\nEnter hours worked: "))
        km_travelled = float(input("Enter km travelled: "))
            
        #Calculates cost
        cost = (CALLOUT_FEE + (hours * PER_HOUR) + (km_travelled * PER_KM))

        #Print costs
        print("\nCallout fee: ${:.2f}".format(CALLOUT_FEE))
        print("Travel fee: ${:.2f}".format((km_travelled * PER_KM)))
        print("Labour fee: ${:.2f}".format((hours * PER_HOUR)))
        print("Total cost for job number {} is: ${:.2f}\n\n".format(job_number, cost))
    except:
        print("\nOops, something broke. Please make sure all inputs are valid.\n\n")
