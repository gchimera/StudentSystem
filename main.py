import csv

from StudentOptions import StudentOptions

vast = StudentOptions()
vast.menu()
n = input("Please enter option: ")


def read_csv(f, cols):
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 1:
            columns = row[0].split()
            yield (columns[c] for c in cols)


if n == 1:
    vast.validate_id()
    vast.generate_password()

elif n == 2:
    with open('students.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

elif n == 3:
    studentID = raw_input("Type student ID to get the details: ")
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        print(filter(lambda x: x[0] in (studentID), list(reader)))

elif n == 4:
     vast.calculateAverage()

elif n == 5:
    vast.highest_student()

elif n == 6:
    vast.change_password()