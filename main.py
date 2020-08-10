import csv

from StudentOptions import StudentOptions
from sys import exit

vast = StudentOptions()


def menu():
    vast.menu()
    n = input("Please enter option: ")

    if n == 1:
        vast.appendToCSV(vast.validate_id(), vast.addStudentName(), vast.addStudentDOB(), vast.generate_password(),
                         vast.addTest(), 0)
        return menu()

    elif n == 2:
        print("All students list: ")
        with open('students.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        return menu()

    elif n == 3:
        studentID = raw_input("Type student ID to get the details: ")
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            print(filter(lambda x: x[0] in studentID, list(reader)))
        return menu()

    elif n == 4:
        vast.calculateAverage()
        return menu()

    elif n == 5:
        vast.highest_student()
        return menu()

    elif n == 6:
        vast.change_password()
        return menu()

    elif n == 7:
        exit()


menu()