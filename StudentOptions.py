import csv
import datetime


def writer(header, data, filename, option):
    with open(filename, "w") as csvfile:
        if option == "write":

            movies = csv.writer(csvfile)
          #  movies.writerow(header)
            for x in data:
                movies.writerow(x)
        # elif option == "update":
        #     writer = csv.DictWriter(csvfile)
        #     writer.writeheader()
        #     writer.writerows(data)
        # else:
        #     print("Option is not known")


class StudentOptions:
    VALID_LENGTH = 7
    newID = ""

    def __init__(self):
        print("Initializzation...")

        filename = "students.csv"
        header = ("StudentID", "Fullname", "DOB", "Password", "Test", "Average")
        data = [
            ("X870052", "Lee Alwan", "31/05/1983", "Empty", 3, 10),
            ("X012253", "Mpiana Utchinga", "31/05/1983", "Empty", 1, 20),
        ]
        writer(header, data, filename, "write")

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
            print x + "\n"

    @staticmethod
    def validate_id():
        StudentOptions.newID = str(raw_input("Type the 7 digits student ID: "))
        if len(StudentOptions.newID) == StudentOptions.VALID_LENGTH:
            print "new student ID: " + StudentOptions.newID
            return str(StudentOptions.newID)
        else:
            print "wrong student ID format: " + StudentOptions.newID
            return StudentOptions.validate_id()

    @staticmethod
    def addStudentName():
        studenName = raw_input("Type student name :")
        print "Student name: " + studenName
        return studenName

    @staticmethod
    def addStudentDOB():
        day = raw_input("Type day of birth (dd): ")
        month = raw_input("Type month of birth (mm): ")
        year = raw_input("Type year of birth (yyyy): ")

        if day.isdigit() and month.isdigit() and year.isdigit():
            dob = datetime.date(int(year), int(month), int(day))
            now = datetime.date(datetime.datetime.now().year,
                                datetime.datetime.now().month,
                                datetime.datetime.now().day)

            dob_before_now = dob < now

            if dob_before_now:

                print "Student date of birthday: " + str(dob)
                return dob
            else:
                print "Incorrect format date"
                return StudentOptions.addStudentDOB()

        else:
            print "Wrong date format!"
            StudentOptions.addStudentDOB()




    @staticmethod
    def addTest():
        score = input("Type test score ")
        if 0 < score < 4:
            print "Test score: " + str(score)
            return score
        else:
            print "Incorrect test score"
        return StudentOptions.addTest()

    @staticmethod
    def calculateAverage():

        index = 0  # each value in each column is appended to a list
        sum = 0

        with open('students.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for lines in csv_reader:
                sum += int(lines[5])
                index += 1

        average = str(sum / index)
        print "The average of the students is: " + str(average)

    @staticmethod
    def highest_student():

        # Calculate the highest student average
        average = []

        with open('students.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for lines in csv_reader:
                average.append(int(lines[5]))

                highest = max(average)

        # Get related student who match with the 'highest' value
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            print("The best student average is: ")
            print(filter(lambda x: x[5] in (str(highest)), list(reader)))

    @staticmethod
    def generate_password():
        newPassword = []
        # The first character of the new password should be the last digit in the ID
        lastChar = StudentOptions.newID[6]
        firstChar = StudentOptions.newID[0]

        for currentdigit in StudentOptions.newID:
            # skip last char
            if currentdigit.isdigit():
                othersint = int(currentdigit)
                lastCharint = int(lastChar)
                next = abs(othersint * lastCharint)
                newPassword.append(next)

        # converting 'newPassword' list of integers into a single integer
        strings = [str(integer) for integer in newPassword]
        a_string = "".join(strings) + firstChar

        return a_string
        print("newPassword: " + a_string)


    @staticmethod
    def change_password():
        with open("students.csv", "r") as f:
            reader = csv.reader(f)
            studentID = raw_input("Type student ID to get the details: ")
            with open("students.csv", "r") as f:
                reader = csv.reader(f)
                student = filter(lambda x: x[0] in (studentID), list(reader))
                print("His/Her current password is: " + student[0][3])  # get the password
                newpassword = raw_input("Type a new password to replace: ")
                student[0][3] = newpassword  # replace password
                print("New password: " + student[0][3])  # get the password

    @staticmethod
    def appendToCSV(studentID, fullname, dob, password, score, average):

        toAdd = [studentID, fullname, dob, password, score, average]

        with open("students.csv", "r") as infile:
            reader = list(csv.reader(infile))
            reader.append(toAdd)


        with open("students.csv", "w") as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)