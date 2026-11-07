from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

def main():
    if len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3 and sys.argv[1] != "-f":
        sys.exit("Invalid usage")

    string = input("Input: ")

    if len(sys.argv) == 1:
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(string))
    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(string))

main()


