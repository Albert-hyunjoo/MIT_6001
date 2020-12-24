# input: annual_salary
# output: 1) savings rate 2) steps in bisection result
# 만약 계속해도 찾을 수 없다면 die ("it is not possible to pay down payment in three years)

annual_salary = int(input("Enter the starting salary: "))

# 전제 조건들

semi_annual_rate = 0.07
r = 0.04 # investment return of r per year
portion_down_payment = 0.25
total_cost = 1000000
total_down_payment = total_cost * portion_down_payment # 250000
current_saving = 0.0

# for bisectional search

high = 1.0
low = 0.0
steps = 0

# 무엇을 해야 할까?
# 먼저 36개월 동안 모을 때 guess를 넣으면 current saving이 나오는 함수를 만들어서
# 그 guess를 비교할 때 bisectional search를 동원해서
# guess <-> low, high 계속 비교해서 올바른 이율 찾아내고 + step counter 써서 step counted

# 36개월 동안 특정 저축률에 따라 current_saving이 나오는 함수

def calculate_saving(current_saving, monthly_salary, saving_rate):
    for months in range(0, 37):
        if months % 6 == 1 and months > 1:
            monthly_salary = monthly_salary * 1.07 # semi_annual_rate
        current_saving = current_saving + monthly_salary * saving_rate + current_saving * 0.04/12
    return current_saving

# print(calculate_saving(current_saving, annual_salary/12, 0.27))

while abs(current_saving - total_down_payment) > 100 :
    saving_rate = (low+high)/2 # 0.5를 처음으로 가정
    current_saving = calculate_saving(current_saving, annual_salary/12, saving_rate)
    if current_saving < total_down_payment:
        low = saving_rate
        current_saving = 0
    elif current_saving > total_down_payment + 100:
        high = saving_rate
        current_saving = 0
    if steps > 100:
        print("It is not possible to pay the down payment in three years")
        break
    steps = steps + 1

if saving_rate != 1.0:
    print("Best saving rate: ", saving_rate)
    print("With current savings: ", current_saving)
else:
    None
