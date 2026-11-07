def main():
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
        try:
            date = input("Date: ").strip()

            month, date = date.split("/", maxsplit=1)

            day, year = date.split("/")
            try:
                if int(day) > 31 or int(day) < 1 or int(month) < 1 or int(month) > 12:
                    pass
                else:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            except ValueError:
                pass

        except ValueError:

            month, date = date.split(" ", maxsplit=1)
            if month in months:
                month = months.index(month) + 1

            try:
                day, year = date.split(", ")
                if int(day) > 31 or int(day) < 1 or int(month) < 1 or int(month) > 12:
                    pass
                else:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            except ValueError:
                pass

main()
