from mentor import Mentor
from student import Student
import random


class CodecoolClass:
    def __init__(self, location, year, students, mentors):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        students = [Student() for _ in range(5)]
        mentors = [Mentor() for _ in range(4)]
        year = random.choice([2015, 2016])
        location = random.choice(["Miskolc", "Budapest", "Krakow"])
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


#    def import_from_csv(self, file_name):
#        file_list = list(csv.reader(open(file_name), delimiter=','))
#        if file_name.split(".")[0] = "mentors":
#            mentors = [Mentor() for _ in file_list]
#            return mentors
#        elif file_name.split(".")[0] = "students":
#            students = [Student() for _ in file_list]
#            return students
#
#    def export_to_csv(self, file_name)
