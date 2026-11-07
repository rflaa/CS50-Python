def main():
    p = percent()
    print(p)

def percent():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            p = int(round((int(x)/int(y))*100))

            if 0 <= p <= 1:
                return "E"
            elif 100 >= p >= 99:
                return "F"
            elif p < 0 or p > 100:
                pass
            else:
                return str(p) + "%"
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except p > 100:
            pass

main()

