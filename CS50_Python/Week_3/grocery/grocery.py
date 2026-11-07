def main():
    list = {}

    while True:
        try:
            item = input().strip().upper()
            if (item in list):
                list[item] += 1
            else:
                list.update({item:1})
        except EOFError:
            for item in sorted(list):
                print(list[item], item)
            break


main()

