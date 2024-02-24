def main():
    fr = input("Fraction: ")
    per = convert(fr)
    print(gauge(per))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            if new_x > new_y:
                continue
        except (ValueError, ZeroDivisionError):
            raise
        else:
            break

    return (100 / new_y) * new_x



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
