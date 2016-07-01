from mentor import Mentor
from student import Student
from person import Person
import random

class CodecoolClass:
    coffee_status = False

    def __init__(self, location, year, students, mentors):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students
        self.stat_morning = None
        self.stat_evening = None

    @classmethod
    def generate_local(cls):
        students = Student.create_by_csv("data/students.csv")
        mentors = Mentor.create_by_csv("data/mentors.csv")
        year = 2016
        location = "Budapest"
        local_class = CodecoolClass(location, year, students, mentors)
        return local_class

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            if full_name == " ".join([student.first_name, student.last_name]):
                return student

    def find_mentor_by_full_name(self, full_name):
        for mentor in self.mentors:
            if full_name == " ".join([mentor.first_name, mentor.last_name]):
                return mentor

    def appoint_mentor(self):
        appointed_mentor = random.choice(self.mentors)
        appointed_mentor.appoint_mentor()

    def export_to_csv(self):
        with open("data/mentors.csv", "a") as wm, open("data/students.csv", "a") as ws:

            pass

    def sum_stats(self, stat_status):
        energy = 0
        skill = 0
        moral = 0
        overall = 0
        number_of_class = len(self.students) + len(self.mentors)

        for mentor in self.mentors:
            energy += mentor.energy_level
            skill += mentor.skill_level
            moral += mentor.moral_level
        for student in self.students:
            energy += student.energy_level
            skill += student.skill_level
            moral += student.moral_level

        overall = energy + skill + moral
        energy = energy//number_of_class
        skill = skill//number_of_class
        moral = moral//number_of_class

        if stat_status == "morning":
            self.stat_morning = overall
        if stat_status == "evening":
            self.stat_evening = overall

        print("""Codecool class state at the {0} is: \n
              Average energy level: {1}
              Average skill level: {2}
              Average moral level: {3}
              Overall class status: {4}""".format(stat_status, energy, skill, moral, overall))
        return overall

    def report_day(self, stat_morning, stat_evening):
        changes = stat_evening - stat_morning
        if changes > 0:
            print("\nCodecool overall status has increased by {0} points.".format(changes) +
                  "\nLet's go to the terrace opening party!!!")
        else:
            print("\nCodecool overall status has decreased by {0} points. ".format(abs(changes)) +
                  "\nLet's do it better tomorrow! 'Gyerünk rakjuk meg!'")

    def drink_coffee(self, limit):
        if CodecoolClass.coffee_status:
            for person in self.students+self.mentors:
                if person.energy_level < limit:
                    person.process([10, "{0}'s energy level is critical. Let's drink coffee! ".format(person.first_name) +
                                    "Energy level: ", "energy_level"])
