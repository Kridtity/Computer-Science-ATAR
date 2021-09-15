#Tax and Wage Calculator
hours_worked = float(input('Enter hours worked: '))
pay_rate = float(input('Enter hourly rate: '))
bonus_rate = float(input('Enter bonus rate or extra loading: '))
bonus_hours = float(input('Enter hours worked with bonus: '))
tax_rate = float(input('Enter tax rate (as decimal): '))

normal_wage = hours_worked * pay_rate
bonus_wage = bonus_hours * bonus_rate
total_wage = normal_wage + bonus_wage
tax = total_wage * 0.3
net_wage = total_wage - tax

print('Base wage: ${:.2f} \nBonus wage: ${:.2f} \nGross wage: ${:.2f} \nTax deducted: ${:.2f} \nNet wage: ${:.2f}'.format(normal_wage, bonus_wage, total_wage, tax, net_wage))
