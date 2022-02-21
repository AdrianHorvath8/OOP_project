from information_system import InformationSystem
import sys

from student_teacher import Student,Teacher

def menu():
    print("Menu:")
    print("0 End program")
    print("1. Create student")
    print("2. Create teacher")
    print("3. Create course")
    print("4. View students")
    print("5. View teachers")
    print("6. View couses")

if __name__=="__main__":
    inf=InformationSystem(teachers=([Teacher("Ladislav","Horvath","Ing"),Teacher("Otilia","Staničiarova","Mgr")]),
    students=([Student("Adrian","Horvath","3.A"),Student("Daniel","Hamrak","3.A")]))
    while True:
        menu()
        decision=int(input("Your chose: "))
        if decision==0:
            sys.exit("Bye")
        if decision==1:
            inf.create_student()
        if decision==2:
            inf.create_teacher()
        if decision==3:
            inf.create_course()
        if decision==4:
            for i in inf.students:
                print(i)
        if decision==5:
            for i in inf.teachers:
                print(i)
        if decision==6:
            for i in inf.courses:
                print(i)
