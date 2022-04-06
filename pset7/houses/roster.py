# TODO
from cs50 import SQL
from sys import argv

# Create database
db = SQL("sqlite:///students.db")

# Check input
if (len(argv) != 2):
    print("Usage: python import.py housename")
    exit(1)
elif(len(argv) == 2):
    house = argv[1]

    # Make a list from databse
    names = (db.execute("SELECT first,middle,last,birth FROM students WHERE house=? ORDER BY last,first ASC", house))

    # Loop over names
    for row in names:

        # If middle name exist
        if row["middle"] != "None":
            first = row["first"]
            middle = row["middle"]
            last = row["last"]
            birth = int(row["birth"])

            fullName = ("{} {} {}, born {}")
            print(fullName.format(first, middle, last, birth))
        else:
            first = row["first"]
            last = row["last"]
            birth = int(row["birth"])

            fullName = ("{} {}, born {}")
            print(fullName.format(first, last, birth))
