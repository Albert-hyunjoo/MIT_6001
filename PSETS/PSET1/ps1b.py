# input :
# 1) annual salary
# 2) percentage of the salary to save, as a decimal
# 3) cost of your dream home

# variables
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of the salary to save, as a decimal: "))
total_cost = int(input("Enter your cost of your dream home: "))
semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

# additional settings
monthly_salary = annual_salary / 12
portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04

# main loops
month = 0
while current_savings < total_down_payment :
    current_savings = current_savings + monthly_salary * portion_saved + current_savings * r/12
    print(current_savings)
    month = month + 1
    if month % 6 == 0:
        monthly_salary = monthly_salary + monthly_salary * semi_annual_rise

print(month)






