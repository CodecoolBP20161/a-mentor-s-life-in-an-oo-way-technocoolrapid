from person import Person
from student import Student
from random import randint


class Assignment:
    def __init__(self, name, student, is_active=False, mentor=None, grade=None):
        self.name = name
        self.student = student
        self.difficulty = randint(5, 10)
        self.grade = grade
        self.mentor = mentor  # mentor who gives grade for the assignment
        self.is_active = is_active
        if is_active:
            self.questions = ["Soooo, what's the deadline?",
                              "How is it related to OOP?",
                              "How many classes do we need to create?"
                              "How old is Humen?"
                              "Can we have a more difficult project?"
                              ]

    def get_grade(self):
        # based on the difficulty of the assignment and the skill level of the student, the assignment gets graded
        morale_of_mentor = 0

        if self.student.skill_level == self.difficulty:
            self.grade = 70
            morale_of_mentor += 2
            reaction = "I can see you worked hard on the project. Nice job! The morale level of mentor increased by 2"
        elif self.student.skill_level < self.difficulty:
            self.grade = 40
            morale_of_mentor -= 7
            reaction = "The assignment contains a few errors, keep trying! The morale level of mentor decreased by 7"
        elif self.student.skill_level > self.difficulty:
            self.grade = 100
            morale_of_mentor = 5
            reaction = "Excellent assignment, keep on rocking! The morale level of mentor increased by 5"
        print("{0}'s assignment, {1} has been graded: {2}%".format(self.student.first_name, self.name, self.grade))
        return [morale_of_mentor, reaction, "moral_level"]

        # return formatted string of the student's name, the name of the assignment and the grade

    def understand_assignment(self, student):
        return student.skill_level >= self.difficulty
            # print("{0} has understood the assignment called {1}".format(student.first_name, self.name))

project = Assignment("A mentor's life in an OOP way", student)
print(project)
print(project.questions)
print(project.get_grade())
print(project.understand_assignment())
