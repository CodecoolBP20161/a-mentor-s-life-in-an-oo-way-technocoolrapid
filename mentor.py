from person import Person
import random

class Mentor(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.responsible = False

    def appoint_mentor(self):
        self.responsible = True
        print("{0} {1} is responsible for the project.".format(self.first_name, self.last_name))
        if randint.random() % 2 == 0:
            self.moral_level += 2
            print("This is going to be a great project, let's do it!")
        else:
            self.moral_level -= 2
            print("Ehh, one more thing to do...")