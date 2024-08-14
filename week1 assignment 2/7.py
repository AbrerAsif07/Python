salary = int(input("Enter current salary = "))
if salary < 10000:
    new_sl = (salary * 5 / 100) + salary
    print(new_sl)
elif salary >= 10000 and salary < 20000:
    new_sl = (salary * 10 / 100) + salary
    print(new_sl)
elif salary >= 20000 and salary < 50000:
    new_sl = (salary * 15 / 100) + salary
    print(new_sl)
else:
    salary >= 50000
    new_sl = (salary * 20 / 100) + salary
    print(new_sl)
#optimised space soln
# salary = float(input("Enter the salary = "))
# if salary < 10000:
#     increment = 0.05
# elif salary <= 20000:
#     increment = 0.10
# elif salary <= 50000:
#     increment = 0.15
# else:
#     increment = 0.20

# updated_salary = salary + (salary * increment)
# print(f"Updated salary = {updated_salary}")