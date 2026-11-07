def convert(a):
    a = a.replace(":)", "\N{slightly smiling face}")
    a = a.replace(":(", "\N{slightly frowning face}")
    return(a)

def main():
    sentence = input("Type in a sentence: ")
    print(convert(sentence))

main()
