from student_teacher import Student,Teacher
from course import Course


class InformationSystem:

    def __init__(self,courses=[], students=[], teachers=[]):
        self.courses=courses
        self.students=students
        self.teachers=teachers

    def create_student(self):
        n=input("Name: ")
        s=input("Surname: ")
        g=input("Grade: ")

        student=Student(n,s,g)
        self.students.append(student)



    def create_teacher(self):
        n=input("Name: ")
        s=input("Surname: ")
        d=input("Degree: ")

        teacher=Teacher(n,s,d)
        self.teachers.append(teacher)
    def create_course(self):
        n=input("Name: ")
        count=0

        for i in self.teachers:
            print(f"{count}. {i}")
            count+=1
        chose=int(input("Chose: "))
        t=self.teachers[chose]

        s=[]
        decision=int(input("How many students do you wanna add: "))
        count=len(self.students)
        for j in range(0,decision):
            for i in range(0,count):
                print(f"{i}. {self.students[i]}")
            chose=int(input("Chose: "))
            s.append(self.students[chose])
        course=Course(n,t,s)
        self.courses.append(course)