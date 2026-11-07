import sys
import tabulate as tab
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    name = sys.argv[1]
    if not(name.endswith(".csv")):
        sys.exit("Not a csv file")
    else:
        try:
            pizzas = []
            with open(name) as file:
                reader = csv.DictReader(file)
                if name == "sicilian.csv":
                    for row in reader:
                        pizzas.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
                elif name == "regular.csv":
                    for row in reader:
                        pizzas.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
        except FileNotFoundError:
            sys.exit("File not found")
        print(tab.tabulate(pizzas, headers="keys", tablefmt="grid"))

