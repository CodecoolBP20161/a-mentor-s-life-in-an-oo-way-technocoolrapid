from person import Person
import random


class Mentor(Person):
    def __init__(self, nick_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nick_name = nick_name
        self.responsible = False

    def appoint_mentor(self):
        self.responsible = True
        print("{0} {1} is responsible for the project.".format(self.first_name, self.last_name))
        if random.randint(0, 1000) % 2 == 0:
            self.moral_level += 2
            print("This is going to be a great project, let's do it!")
            print("The moral level of {0} {1} has increased by 2.".format(self.first_name, self.last_name))
        else:
            self.moral_level -= 2
            print("Ehh, one more thing to do...")
            print("The moral level of {0} {1} has decreased by 2.".format(self.first_name, self.last_name))
