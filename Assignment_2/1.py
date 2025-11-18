salary = int(input("Enter the salary: "))
tax = 0

if (salary < 30000):
    tax = "5%"
elif (salary >=30000 and salary < 70000):
    tax = "15%"
elif (salary >= 70000):
    tax = "25%"
else:
    print("Default Value Entered")

print(tax)