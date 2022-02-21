from student_teacher import Teacher,Student


class Course:
    def __init__(self, name,teacher=Teacher,students=[]):
        self.name=name
        self.teacher=teacher
        self.students=students


    def __str__(self):
        dalimiter="\n\t"
        return f"Course {self.name}\n\t{self.teacher}\n\t{dalimiter.join([student.__str__() for student in self.students])}"

    def add_student(self,value):
        self.students.append(value)