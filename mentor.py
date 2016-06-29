from person import Person


class Mentor(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.responsible = False

    def appoint_mentor(self):
        self.responsible = True
        print("{0} {1} is responsible for the project.".format(self.first_name, self.last_name))
