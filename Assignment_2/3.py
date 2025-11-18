num = int(input("Enter the Number : "))

def digit_printing(num):
    if num < 0:
        print("Not applicable for negative values")
        return
    while num > 0:
        print(num%10, end=", ")
        num = num//10

digit_printing(num)
