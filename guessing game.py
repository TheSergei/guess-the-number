import random

def guess_the_number():
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("guess the number between 1 and 100!: "))

        if guess > secret_number:
            print("too high! try again.")
        elif guess < secret_number:
            print("too low! try again.")
        else:
            print("congratulations! you got it!")
            break

if __name__ == "__main__":
    guess_the_number()