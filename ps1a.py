def months_needed(annual_salary, portion_saved, total_cost):
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    monthly_salary = annual_salary * 1/12
    monthly_saving = monthly_salary * portion_saved
    months_passed = 0
    while current_savings < portion_down_payment:
        months_passed += 1
        current_savings += 0.04/12 * current_savings + monthly_saving
    return months_passed
a = int(input('Enter your annual salary: '))
b = input('Enter the percent of your salary to save, as a decimal: ')
c = int(input('Enter the cost of your dream home: '))
b_int = float('0'+b)
print('Numbers of months: {:d}'.format(months_needed(a,b_int,c)))

