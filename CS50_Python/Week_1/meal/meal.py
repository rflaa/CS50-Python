def convert(time):
    time = time.lower().strip()
    hours, minutes  = time.split(":")

    if("p.m." in minutes):
        hours = float(hours) + 12
        minutes = minutes.removesuffix(" p.m.")
    elif("a.m." in minutes):
        minutes = minutes.removesuffix(" a.m.")

    hours = float(hours)
    minutes = float(minutes)/60
    final = hours + minutes

    return(final)

def main():
    time = input("What time is it? ")

    if(7 <= convert(time) <= 8):
        print("breakfast time")
    elif(12 <= convert(time) <= 13):
        print("lunch time")
    elif(18 <= convert(time) <= 19):
        print("dinner time")
    else:
        print("")

if __name__ == "__main__":
    main()
