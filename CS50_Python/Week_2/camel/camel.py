def convert(camel):
    for i in range(len(camel)):
        if camel[i].islower():
            print(camel[i], end="")
        else:
            print("_" + camel[i].lower(), end="")
    print()

def main():
    camel = input("camelCase: ")
    convert(camel)

main()
