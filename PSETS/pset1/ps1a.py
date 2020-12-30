# input :
# 1) annual salary
# 2) percentage of the salary to save, as a decimal
# 3) cost of your dream home

# variables
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of the salary to save, as a decimal: "))
total_cost = int(input("Enter your cost of your dream home: "))

# additional settings
portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04

# main loops
month = 0
while current_savings <= total_down_payment :
    current_savings = current_savings + annual_salary/12 * portion_saved + current_savings * r/12
    month = month + 1

print(month)




