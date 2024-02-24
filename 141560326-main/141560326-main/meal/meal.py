def main():
    answ = input("What time is it? ")
    time = convert(answ)

    if time <= 8 and time >= 7:
        print("breakfast time")
    elif time<= 13 and time >= 12:
        print("lunch time")
    elif time<=19 and time >= 18:
        print("dinner time")
def convert(time):
    am_pm = ""
    if "a.m." in time or "p.m." in time:
        hours_minutes , am_pm = time.split(" ")
        hours , minutes = hours_minutes.split(":")
    else :
        hours , minutes = time.split(":")

    if am_pm == "p.m.":
        hours = float(hours) + 12

    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()