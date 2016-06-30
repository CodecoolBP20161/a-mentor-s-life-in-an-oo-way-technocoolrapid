from mentor import Mentor
from student import Student
import random


class CodecoolClass:
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

    def export_to_csv(self):  # append vagy write a jobb megoldás
        with open("data/mentors.csv", "a") as wm, open("data/students.csv", "a") as ws:

            pass

    def sum_stats(self, stat_status):  # kérdés hogyan írja a stat_evening stat_morning ot???

        energy = 0
        skill = 0
        moral = 0
        overall = 0

        for mentor in self.mentors:
            energy += mentor.energy_level
            skill += mentor.skill_level
            moral += mentor.moral_level
        for student in self.students:
            energy += student.energy_level
            skill += student.skill_level
            moral += student.moral_level

        overall = energy + skill + moral
        if stat_status == "morning":
            self.stat_morning = overall
        if stat_status == "evening":
            self.stat_evening = overall

        print("""Codecool class state at the {0} is : \n
              energy level:{1}
              skill level:{2}
              moral level:{3}
              overall: {4}""".format(stat_status, energy, skill, moral, overall))
        return overall

    def report_day(self, stat_morning, stat_evening):
        changes = stat_morning - stat_evening
        if changes < 0:
            print("Codecool overall status has changed by the day {0} points.Let's go to terrace opening party!!!".format(changes))
        else:
            print("Codecool overall status has changed by the day {0} points.Let's do more harder. 'Gyerünk rakjuk meg'".format(changes))

    def attendance_check(self):
        pass
