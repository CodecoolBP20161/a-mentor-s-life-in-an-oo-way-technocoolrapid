from person import Person
from student import Student
from random import randint


class Assignment:
    def __init__(self, name, student, is_active=False, grade=None):
        self.name = name
        self.difficulty = randint(5, 10)
        self.grade = grade
        self.is_active = is_active
        # student = student object
        self.questions = []

        # questions = ["Soooo, what's the deadline?",
        #              "How is it related to OOP?",
        #              "How many classes do we need to create?"
        #              "How old is Humen"?
        #             ]
        # randchoice?

    def get_grade(self):
        # based on the difficulty of the assignment and the skill level of the student, the assignment gets graded

        if student.skill_level == self.difficulty:
            self.grade = 70
        elif student.skill_level < self.difficulty:
            self.grade = 40
        elif student.skill_level > self.difficulty:
            self.grade = 100
        print("{0}'s assignment, {1} has been graded: {2}%".format(student.first_name, self.name, self.grade))
        return self.grade

        # return formatted string of the student's name, the name of the assignment and the grade

    def understand_assignment(self):
        if student.skill_level >= self.difficulty:
            print("{0} has understood the assignment called {1}".format(student.first_name, self.name))
            return student
        else:
            print("{0} has not understood the assignment called {1}".format(student.first_name, self.name))

student = Student(False)
project = Assignment("A mentor's life in an OOP way", student)
print(project)
print(project.questions)
print(project.get_grade())
print(project.understand_assignment())
