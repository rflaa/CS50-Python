def main():
    print("Amount Due: 50")
    due = 50

    while due > 0:
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            due -= coin
            if due > 0:
                print("Amount Due:", due)
        else:
            if due > 0:
                print("Amount Due:", due)

    print("Change Owed:", due * -1)

main()


