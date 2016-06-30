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
            print("Student {0} understood the project. ".format(self.first_name)
                  + ("His" if self.gender == "Male" else "Her") + " morale increased by 1.")
        else:
            self.moral_level -= 1
            print("Student {0} did not understand the project. ".format(self.first_name)
                  + ("His" if self.gender == "Male" else "Her")+ " morale decreased by 1.")
