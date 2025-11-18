num = int(input("Enter the Number : "))

def digit_printing(num):
    if num < 0:
        print("Not applicable for negative values")
        return
    count = 0
    while num > 0:
        count += 1
        num = num//10
    print("Total digits:", count)


digit_printing(num)