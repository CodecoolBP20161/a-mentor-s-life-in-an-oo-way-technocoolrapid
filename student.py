from person import Person
import random


class Student(Person):
    def __init__(self, *args, **kwargs):
        self.late = random.choice([True, False])
        self.understood_project = False
        super().__init__(*args, **kwargs)

    @classmethod
    def create_by_csv(cls, path):
        student_objects = []
        with open(path, "r") as f:
            for student in f:
                if student.strip() is not None:
                    student = student.replace("\n", "")
                    student_objects.append(Student(*student.split(",")))
        return student_objects

    def understanding_project(self, understood):
        self.understood_project = understood
        if self.understood_project:
            self.moral_level += 1
            print("Student %s understood the project. His/her morale increased by 1." % self.first_name)
        else:
            self.moral_level -= 1
            print("Student %s did not understand the project. His/her morale decreased by 1." % self.first_name)
