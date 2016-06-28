# from mentor import Mentor
from student import Student
import random


class CodecoolClass:
    def __init__(self, location, year, students):
        self.location = location
        self.year = year
#        self.mentors = []
        self.students = students

    @classmethod
    def generate_local(cls):
        students = [Student(True) for _ in range(5)]
        year = random.choice([2015, 2016])
        location = random.choice(["Miskolc", "Budapest", "Krakow"])
        local_class = CodecoolClass(location, year, students)
        return local_class

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            name = " ".join([student.first_name, student.last_name])
            if name == full_name:
                return student

#    def find_mentor_by_full_name(self, full_name):
#        for mentor in self.mentors:
#            name = " ".join([mentor.first_name, mentor.last_name])
#            if name == full_name:
#                return mentor
