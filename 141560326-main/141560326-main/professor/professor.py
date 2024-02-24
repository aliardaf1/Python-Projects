import random


def main():
    score = 0
    question_number = 0
    level = get_level()
    while question_number != 10 :
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        tries = 0

        while True:
            answer = int(input(f"{x} + {y} = "))
            if answer != result:
                print("EEE")
                tries += 1
            else :
                question_number += 1
                score += 1
                break
            if tries == 3 :
                print(f"{x} + {y} = {result}")
                question_number += 1
                break

    print(f"Score: {score}")
def get_level():
    while True:
        try :
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else :
                continue
        except ValueError:
            pass


def generate_integer(level):
    if int(level) == 1:
        return random.randint(0,9)
    elif int(level) == 2:
        return random.randint(10,99)
    elif int(level) == 3:
        return random.randint(100,999)
    else :
        raise ValueError

if __name__ == "__main__":
    main()