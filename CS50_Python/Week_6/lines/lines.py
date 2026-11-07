import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    name = sys.argv[1]
    if not(name.endswith(".py")):
        sys.exit("Not a Python file")
    else:
        try:
            with open(name, "r") as file:
                count = 0
                for line in file:
                    if line.lstrip().startswith("#"): continue
                    elif line.isspace(): continue
                    else: count += 1
        except FileNotFoundError:
            sys.exit("File not found")

    print(count)


