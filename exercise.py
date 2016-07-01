from codecool_class import CodecoolClass
from person import Person
from mentor import Mentor
from student import Student
from event import Event
from study import Study
from atmosphere import Athmosphere
from assignment import Assignment
import random

codecool_bp = CodecoolClass.generate_local()
codecool_bp.sum_stats("morning")
print(codecool_bp.stat_morning)
# print(codecool_bp)
# for i in codecool_bp.mentors:
#     i.process(Event(-3, "{0} attending on the meeting. Energy level: ".format(i.full_name)).process_event)
codecool_bp.appoint_mentor()
active_mentor = next(i for i in codecool_bp.mentors if i.responsible)
# print(codecool_bp.students[1].late)
late = len([i for i in codecool_bp.students if i.late])
print(late)
