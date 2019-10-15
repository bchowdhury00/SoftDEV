#Biraj Chowdhury
#SoftDev Period 9
#K18 Average/Databases/Accessing and manipulating data
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="stu.db"
COURSE_FILE = "courses.csv";
STUDENT_FILE = "students.csv";

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#delete tables if they exist when compiling
c.execute("DROP TABLE IF EXISTS courses")
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS stu_avg")

#create the tables for courses and students
with open(STUDENT_FILE, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     test = "CREATE TABLE students (name TEXT,age INTEGER, id INTEGER);"
     c.execute(test)
     for row in reader:
         c.execute("INSERT INTO students VALUES (?, ?, ?)", (row["name"], row["age"], row["id"]))

with open(COURSE_FILE, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      test = "CREATE TABLE courses (code TEXT,mark INTEGER, id INTEGER);"
      c.execute(test)
      for row in reader:
          c.execute("INSERT INTO courses VALUES (?, ?, ?)", (row["code"], row["mark"], row["id"]))


def getStudentID(name):
    cur = c.execute("SELECT id FROM students WHERE name = ?", [str(name)])
    return cur.fetchone()[0] #select first element in the chosen row

print(getStudentID("armin"))

def getStudentGrade(name):
    cur = c.execute("SELECT mark FROM courses WHERE id = ?", [getStudentID(name)])
    allGrades = cur.fetchall()
    return allGrades

print(getStudentGrade("armin"))

def getAverage(name):
    allGrades = getStudentGrade(name)
    average = 0
    length = 0

    for row in allGrades:
        grade = row[0] #the grade is the first element in that row
        average += grade
        length += 1;
    return average / length;

print(getAverage("armin"))



def displayStudent(name):
    return "name: " + name + " id: " + str(getStudentID(name)) + " average: " + str(getAverage(name))

print(displayStudent("armin"))


#Creating table
c.execute("CREATE TABLE stu_avg (id INTEGER, avg INTEGER);")
cur = c.execute("SELECT name FROM students")
allNames = cur.fetchall()
for row in allNames:
    name = row[0]
    c.execute("INSERT INTO stu_avg VALUES (?, ?)", (str(getStudentID(name)), str(getAverage(name))))

def addcourse(code, mark, id):
    c.execute("INSERT INTO courses VALUES (?, ?, ?)", (str(code), str(mark), str(id)))

addcourse("newClass", 100, 0)
db.commit() #save changes
db.close()  #close database
