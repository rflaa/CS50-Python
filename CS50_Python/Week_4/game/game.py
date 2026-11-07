from random import randint
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            number = randint(1, level)
            break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input("Guess: "))

            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

main()
