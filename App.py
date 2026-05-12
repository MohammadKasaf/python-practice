employees = [

    ("Ali", "IT", 50000),
    ("Ahmed", "HR", 70000),
    ("Sara", "IT", 60000),
    ("John", "Finance", 80000),
    ("Areeba", "HR", 75000)
]

#Print all employee names
print("Print all employee names:")
for info in employees:
    print(info[0])

#find highest salary employee
print("Print highest employee name:")
highest_salary=0
employee_name=""
for info in employees:
    if info[2]>highest_salary:
        highest_salary = info[2]
        employee_name = info[0]

print(f"highest salary employee is {employee_name} and his salary is {highest_salary}")