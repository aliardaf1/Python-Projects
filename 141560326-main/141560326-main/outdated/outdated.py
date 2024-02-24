months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()

    if "/" in date :
        month , day , year = date.split("/")
        if not month.isdecimal():
            continue
        if int(day) > 31 or int(month) > 12:
            continue
        else :
            break
    elif "," in date :
        month_day , year = date.split(",")
        month2 , day = month_day.split(" ")
        year = year.strip()
        if month2 in months:
            if int(day) > 31 :
                continue
            month = months.index(month2)+1
            break

print(f"{int(year):02}" + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")