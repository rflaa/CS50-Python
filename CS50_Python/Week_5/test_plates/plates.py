def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #checks if first and second chars are letters
    #checks if there are no punctuation marks or symbols
    if len(s) > 6 or len(s) < 2:
        return False
    #checks if length is valid
    elif not s[0].isalpha() or not s[1].isalpha() or not s.isalnum():
        return False
    #checks if every number is followed by another
    #(meaning no numbers in bewtween)
    else:
        for i in range(len(s)-1):
            if s[i].isdigit() and not s[i+1].isdigit():
                return False
            if i > 0 and s[i] == "0" and not s[i-1].isdigit():
                return False
        return True

if __name__ == "__main__":
    main()
