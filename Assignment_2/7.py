while True:
    num = input("Enter a number (Quit to exit): ")
    if num == "Quit":
        break
    else:
        num = int(num)
        if num > 0:
            print("Positive Number")
        else:
            print("Negative Number")