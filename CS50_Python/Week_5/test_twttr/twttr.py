def main():
    string = input("Input: ")
    print("Output:", shorten(string))

def shorten(word):
    word = word.strip(" ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for letter in vowels:
        word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
