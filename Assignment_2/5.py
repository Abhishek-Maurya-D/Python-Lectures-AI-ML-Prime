num = int(input("Enter the Number : "))

def digit_printing(num):
    if num < 0:
        print("Not applicable for negative values")
        return
    sum = 0
    while num > 0:
        digit = num%10
        sum = sum + digit
        num = num//10
    print("Sum of digits: ", sum)

digit_printing(num)
