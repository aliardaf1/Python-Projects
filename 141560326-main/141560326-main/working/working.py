import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"^(\d[1-2]?):?([0-5][0-9])? (AM|PM) to (\d[1-2]?):?([0-5][0-9])? (AM|PM)$", s
    )
    if matches:
        groups = matches.groups()
        if groups[2] == "PM":
            hours1 = int(groups[0]) + 12
        else:
            if int(groups[0]) <= 9:
                hours1 = f"0{groups[0]}"
            else:
                hours1 = f"{groups[0]}"
        if groups[5] == "PM":
            hours2 = int(groups[3]) + 12
        else:
            if int(groups[3]) <= 9:
                hours2 = f"0{groups[3]}"
            else:
                hours2 = f"{groups[3]}"
        if groups[1] == None:
            minutes1 = "00"
        else:
            minutes1 = groups[1]
        if groups[4] == None:
            minutes2 = "00"
        else:
            minutes2 = groups[4]
        if groups[0] == "12":
            if groups[2] == "AM":
                hours1 = "00"
            else:
                hours1 = "12"
        if groups[3] == "12":
            if groups[5] == "AM":
                hours2 = "00"
            else:
                hours2 = "12"

        return f"{hours1}:{minutes1} to {hours2}:{minutes2}"
    else:
        raise ValueError("Wrong")



if __name__ == "__main__":
    main()