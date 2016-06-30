import random


class Person:

    def __init__(self, fn, ln, dob, gender):
        self.first_name = fn
        self.last_name = ln
        self.year_of_birth = dob
        self.gender = gender
        self.energy_level = random.randint(50, 70)
        self.moral_level = random.randint(20, 30)
        self.skill_level = random.randint(5, 10)
        self.hungry = random.choice([True, False])

    def process(self, args):
        if args[2] == "energy_level":
            stat = self.energy_level
            self.energy_level += args[0]
        elif args[2] == "skill_level":
            stat = self.skill_level
            self.skill_level += args[0]
        else:
            stat = self.moral_level
            self.moral_level += args[0]
        print(args[1] + str(stat))

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
