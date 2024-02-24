def main():
    answer = input("Greetings:")
    val = value(answer)
    print(f"${val}")

def value(greetings):
    if greetings.lower().strip().startswith("h"):
        if greetings.lower().strip().startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
