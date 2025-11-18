def game():
    secret_number = 43
    while True:
        guess = int(input("Enter the number: "))

        if guess < secret_number:
            print("Too Low")
        elif guess >secret_number:
            print("Too High")
        else:
            print("Congratulations! You guessed it right.")
            break

game()