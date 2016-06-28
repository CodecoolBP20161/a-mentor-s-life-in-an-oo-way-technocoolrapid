import random


class Person:

    def __init__(self):
        fn = random.choice(["Bela", "David", "Gergo", "Reka", "Lilla", "Barbara"])
        self.first_name = fn
        self.last_name = random.choice(["Kocsis", "Kovacs", "Feher", "Nyiro", "Polonkai"])
        self.year_of_birth = random.randint(1985, 1998)
        self.gender = "Male" if fn in ["Bela", "David", "Gergo"] else "Female"
        self.energy_level = random.randint(50, 70)
        self.moral_level = random.randint(20, 30)
        self.skill_level = random.randint(5, 10)
        self.hungry = False

    def process(self, args):
        if args[2] == "energy_level":
            self.energy_level += args[0]
        elif args[2] == "skill_level":
            self.skill_level += args[0]
        else:
            self.morale += args[0]
        print(args[1] + args[0])
