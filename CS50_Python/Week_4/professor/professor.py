import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                elif i == 2:
                    print("EEE")
                    print(f"{x} + {y} = {x+y}")
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass

    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if 1 <= level <= 3:
                return int(level)

        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
        return number
    elif level == 2:
        number = random.randint(10, 99)
        return number
    elif level == 3:
        number = random.randint(100, 999)
        return number
    else:
        raise ValueError

if __name__ == "__main__":
    main()
