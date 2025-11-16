principal = input("Enter the Principal Amount: ")
rate = input("Enter the rate of interest: ")
time = input("Enter the time period (year) : ")

principal = float(principal)
rate = float(rate)
time = float(time)

simple_interest = (principal * rate * time)/100

print("The simple interest is:", simple_interest)
# This program calculates the simple interest based on user input and prints the result.
