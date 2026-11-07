def main():
    string = input("Input: ")
    print("Output:", end="")
    print(shorten(string))

def shorten(word):
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            continue
        elif word[i] == "A" or word[i] == "E" or word[i] == "I" or word[i] == "O" or word[i] == "U":
            continue
        else:
            final[i] = word[i]
    return final

if __name__ == "__main__":
    main()
