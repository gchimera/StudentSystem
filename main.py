import csv
from collections import defaultdict

from StudentOptions import StudentOptions

StudentOptions.menu()
n = input("Please enter option: ")

def read_csv(f, cols):
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 1:
            columns = row[0].split()
            yield (columns[c] for c in cols)


if n == 1:
    vast = StudentOptions(input("Type student ID: "))
    vast.validate_id()
    # vast.addStudentDOB()
    # vast.addTest()

    #vast.calculateAverage()
elif n == 2:
    with open('students.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)