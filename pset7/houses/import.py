import csv
from cs50 import SQL
from sys import argv


def main(argv):

    # Check command-line-argument
    if len(argv) != 2:
        print("Usage: python import.py csvfilename")
        exit(1)

    # Create Database
    open("students.db", "w").close()
    db = SQL("sqlite:///students.db")

    # Create table
    db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMBERIC)")

    # Open csvfile to read
    with open(argv[1], "r") as csvfile:

        # Create dictreader
        reader = csv.DictReader(csvfile)

        # Loop over row
        for row in reader:
            names = []
            names.append(row["name"].split())
            namesArray = names[0]
            if len(namesArray) == 2:
                middle = "None"
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?,?,?,?,?)",
                           namesArray[0], middle, namesArray[1], row["house"], int(row["birth"]))
            if len(namesArray) == 3:
                db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?,?,?,?,?)",
                           namesArray[0], namesArray[1], namesArray[2], row["house"], int(row["birth"]))


if __name__ == "__main__":
    main(argv)