from emoji import emojize

def main():
    string = input("Input: ")
    print(emojize(string, language="alias"))

main()
