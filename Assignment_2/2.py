num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1 > num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

if (num1 % 2 != 0):
    num1 += 1

while num1 <= num2:
    print(num1)
    num1 += 2

