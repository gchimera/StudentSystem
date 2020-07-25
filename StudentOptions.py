from random import randint
import csv
import os
import datetime

class StudentOptions:
    VALID_LENGTH = 7
    newID = ""

    def __init__(self, studentid):
        self.newID = studentid

    @staticmethod
    def menu():
        menu_fields = [
            '************************ \n',
            "* Student System * \n",
            "************************ \n",
            "* 1) Add A Student     * \n",
            "* 2) List all Students     * \n",
            "* 3) View A Student's Details     * \n",
            "* 4) Calculate Overall Average    * \n",
            "* 5) View highest scoring student * \n",
            "* 6) Change Password     * \n",
            "* 7) Create Dictionary   * \n",
            "* 8) Exit     *",
            "************************ \n",
        ]

        for x in menu_fields:
            print(x + "\n")

    @staticmethod
    def validate_id():
        if len(StudentOptions.newID) == StudentOptions.VALID_LENGTH:
            print("new student ID: " + StudentOptions.newID)
            return "new student ID: " + str(StudentOptions.newID)
        else:
            print("wrong student ID format: " + StudentOptions.newID)
            return ""

    @staticmethod
    def addStudentName():
        studenName = input("Type student name ")
        print("Studentname: " + studenName)
        return studenName

    @staticmethod
    def addStudentDOB():
        day = input("Type day ")
        month = input("Type month ")
        year = input("Type year ")

        dob = datetime.date(year, month, day)
        now = datetime.date(datetime.datetime.now().year,
                            datetime.datetime.now().month,
                            datetime.datetime.now().day)

        dob_before_now = dob < now

        if dob_before_now:

            print("Student date of birthday: " + str(dob))
            return dob
        else:
            print("Incorrect format date")

    @staticmethod
    def addTest():
        score = input("Type test score ")
        if 0 < score < 4:
            print("Test score: " + str(score))
            return score
        else:
            print("Incorrect test score")

    @staticmethod
    def calculateAverage():

        index = 0  # each value in each column is appended to a list
        sum = 0

        with open('students.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for lines in csv_reader:
                print(lines[5])
                sum += int(lines[5])
                index += 1

        average = str(sum/index)
        print(str(average))

    @staticmethod
    def generate_password():
            newPassword = []
            # The first character of the new password should be the last digit in the ID
            lastChar = StudentOptions.newID[6]
            print (lastChar)

            for othersdigits in StudentOptions.newID:
                #skip last char
                if othersdigits != lastChar:
                    print(othersdigits)
                    next = abs(othersdigits*lastChar)
                    print(next)
                    newPassword.append(next)

            print("newPassword: " + newPassword)



