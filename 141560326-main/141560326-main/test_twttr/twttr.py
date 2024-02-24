def main():
    word = input("Input: ")
    new = shorten(word)
    print(new)

def shorten(word):
    new_word = ""
    for i in word:
        if (
            i == "A"
            or i == "E"
            or i == "I"
            or i == "O"
            or i == "U"
            or i == "a"
            or i == "e"
            or i == "i"
            or i == "o"
            or i == "u"
        ):
            continue
        else:
            new_word += i
    return new_word


if __name__ == "__main__":
    main()
