import sys
import csv

if len(sys.argv) < 3: sys.exit("Too few command-line arguments")
if len(sys.argv) > 3: sys.exit("Too many command-line arguments")
else:
    try:
        before = sys.argv[1]
        after = sys.argv[2]
        students = []
        with open(before, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                lname, fname = row["name"].split(", ")
                students.append({"first name": fname, "last name": lname, "house": row["house"]})
        with open(after, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
            writer.writerow({"first name": "first",
                             "last name": "last",
                             "house": "house"})
            for student in students:
                writer.writerow({"first name": student["first name"],
                                 "last name": student["last name"],
                                 "house": student["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")
