
from person import Person

class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade=grade

    def __str__(self):
        return (f"Student= Name: {self.name}, Surname: {self.surname}, Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, surname, degree):
        super().__init__(name, surname)
        self.degree=degree

    def __str__(self):
        return (f"Teacher= Name: {self.name}, Surname: {self.surname}, Degree: {self.degree}")