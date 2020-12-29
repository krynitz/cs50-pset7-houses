import csv
from sys import argv, exit
import cs50


def main():
    open_files()

    with open(argv[1]) as test:
        tester = csv.DictReader(test)
        for row in tester:

            # split names into a list of 2 or 3 elements
            s = row["name"].split(' ')

            # convert birth to integer
            birth = int(row["birth"])

            # Check for how many names and insert into table accordingly
            if len(s) == 3:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                           s[0], s[1], s[2], row["house"], birth)
            else:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                           s[0], None, s[1], row["house"], birth)


# function to open all the files and check that everything is right
def open_files():
    # check and exit if right number of arguments not found
    if len(argv) != 2:
        print("Invalid number of command line arguments")
        exit(1)

    # assign database to variable
    global db
    db = cs50.SQL("sqlite:///students.db")


main()
