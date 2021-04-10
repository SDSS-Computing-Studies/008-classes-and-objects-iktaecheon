#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grades = []
    # properties should be listed first

    def __init__(self, name, studentNumber, grade, courses=[], grades=[]): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade
        self.courses = courses
        self.grades = grades

    def __del__(self):
        print("Shutting down")

    def getHonorRoll(self):
        x = self.grades
        x.sort()
        honorgrades = x[-1]+x[-2]+x[-3]+x[-4]+x[-5]
        honorgrades = honorgrades/5
        honorgrades = int(honorgrades)
        if honorgrades >= 86:
            return True
        else:
            return False

    def showCourses(self):
        x = self.courses
        y = print(self.courses)
        return y

    def showGrade(self, ind):
        x = self.courses
        courses = x[ind]
        y = self.grades
        grades = y[ind]
        show = print("{} has a {}percent in {}.".format(self.name, str(grades), str(courses)))
    
    def getCourses(self, x):
        self.courses = x
    
    def getGrades(self, y):
        self.grades = y
    
    def average(self):
        x = self.grades
        y = len(x)
        z = 0
        for i in range(0,y):
            a = x[i]
            z = z+a
        z = z/y
        return z


def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()