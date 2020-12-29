import cs50
from sys import exit, argv

def main():
    open_files()

    students = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last, first", argv[1])

    for s in students:
        if s["middle"] == None:
            print(f"{s['first']} {s['last']}, born {s['birth']}")
        else:
            print(f"{s['first']} {s['middle']} {s['last']}, born {s['birth']}")


def open_files():
    # check and exit if right number of arguments not found
    if len(argv) != 2:
        print("Invalid number of command line arguments")
        exit(1)

    # assign database to variable
    global db
    db = cs50.SQL("sqlite:///students.db")

main()
