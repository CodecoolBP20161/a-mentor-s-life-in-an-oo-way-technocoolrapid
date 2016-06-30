from codecool_class import CodecoolClass
from person import Person
from mentor import Mentor
from student import Student
from event import Event
from study import Study
from atmosphere import Athomosphere
from assignment import Assignment
import random


codecool_bp = CodecoolClass.generate_local()
codecool_bp.sum_stats("morning")
input("")
print("A typical day @Codecool starts with a mentors' discussion about that week's assignment.")
input("")
# event mentor discussion
for i in codecool_bp.mentors:
    event = Event(random.randint(-3, 4), "{0} is attending the meeting. Energy level: ".format(i.full_name))
    i.process(event.process_event())
codecool_bp.drink_coffee(50)
input("")
print("One of the mentors gets appointed to be responsible for the week's project: ")
# event "This week ..... mentor got appointed. Hooraaay!"
# appointing mentor of the week
codecool_bp.appoint_mentor()
active_mentor = next(i for i in codecool_bp.mentors if i.responsible)
input("")
print('''It's 8.40 and the office is almost empty.
Oh, wait, I can see someone drinking their morning coffee in the kitchen.
The students start to arrive very very slowly. Soothing music is playing in the background.''')
input("")
print("GONG!")
input("")
print("Who's here already? Let's check the attendance!")
input("")
# script attendance check (late students)
late = len([i for i in codecool_bp.students if i.late])
event = Athomosphere(-2, "Oh, no, {0} students are late. Morale: ".format(late),
                     -3, "{0} carries out roll attendance. Energy level: ".format(active_mentor.nick_name))
active_mentor.process(event.process_event())
active_mentor.process(event.process_atmosphere())
active_project = Assignment("A mentor's life in an OOP way", None, True, active_mentor)  # args: name, student, is_active, mentor
event = Event(-3, "{0} announces the project for the week. Energy level: ".format(active_mentor.nick_name))
active_mentor.process(event.process_event())
codecool_bp.drink_coffee(50)
input("")
print('"Well, this week\'s assignment will be: {0}"'.format(active_project.name))
input("")
print("Let's see whether our students are able to understand it right away.")
input("")
for i in codecool_bp.students:
    i.understanding_project(active_project.understand_assignment(i))
codecool_bp.drink_coffee(50)
input("")
print("If you have any questions regarding the project ask away! - says {0}".format(active_mentor.nick_name))
input("")
for _ in range(3):
    stud = random.choice(codecool_bp.students)
    event = Study(2, "This was indeed a good question. Skill level: ",
                  -3, "{0} asks THE question bugging ".format(stud.full_name)
                  + ("him" if stud.gender == "Male" else "her") + " for so long! Energy level: ")
    stud.process(event.process_event())
    print(active_project.questions.pop(random.randrange(len(active_project.questions))))
    stud.process(event.process_study())
    print("\n")
codecool_bp.drink_coffee(50)
input("")
print("Do not worry, those who still do not understand will have a chance to discuss with the mentors after school.")
input("")
print('''It's noon already! Time surely flies when you are having fun! Let's have lunch, shall we?
It seems that some of the class is not hungry. They can pass time by playing some table football!''')
input("")
for pers in random.sample(codecool_bp.students + codecool_bp.mentors, 5):
    if pers.hungry:
        event = Athomosphere(3, "Beer is awesome as usual. Morale: ",
                             15, "{0} had some tasty food. Yummy! Energy level: ".format(pers.full_name))
    else:
        event = Athomosphere(5, "And " + ("he" if pers.gender == "Male" else "she")
                             + " didn't need to crawl under the table! Morale: ",
                             -2, "{0} had an intense match at the table. Hooray! Energy level: ".format(pers.full_name))
    pers.process(event.process_event())
    pers.process(event.process_atmosphere())
    print("\n")
codecool_bp.drink_coffee(50)
input("")
print("Lunch break is over, let's get down to business again!")
print("Next on the schedule is discussing the evaluation criteria for the project.")
print("In Codecool we do everything democratically, students and mentors together, the criteria is no exception.")
input("")
for stud in random.sample(codecool_bp.students, 4):
    # stud = random.choice(codecool_bp.students)
    event = Study(3, "This intense brainstorming had good effects on " + ("him." if stud.gender == "Male" else "her.")
                  + " Skill level: ", -2, "{0} had an amazing idea for the evaluation criteria. Energy level: "
                  .format(stud.full_name))
    stud.process(event.process_event())
    stud.process(event.process_study())
codecool_bp.drink_coffee(50)
input("")
print("It is now time to get some real work done! If all goes well everybody will be happy in the end.")
input("")
for i in codecool_bp.students:  # only those students who actually understood the project?
    event = Study(4, ("He" if i.gender == "Male" else "She") + " is getting the hang of it. Skill level: ",
                  -7, "{0} is working on the assignment. Energy level: ".format(i.full_name))
    i.process(event.process_event())
    i.process(event.process_study())

print("\nPhew, this was some real hard work, but we all did a good job!")
input("")
# generating random number of assignment instances, giving it to random students and a randomly chosen inactive mentor
assignments = []
inactive_mentors = [i for i in codecool_bp.mentors if i is not active_mentor]
for j in ["100doors", "phone_numbers", "car_dealer"]:
    for i in range(random.randint(4, 7)):
        stud = None
        while stud is None or stud in [i.student for i in assignments if i.name == j]:
            stud = random.choice(codecool_bp.students)
        assignments.append(Assignment(j, stud, random.choice(inactive_mentors)))
codecool_bp.drink_coffee(40)
mentor = random.choice(inactive_mentors)
if len(assignments) < 17:
    event = Athomosphere(3, "This is not as much as I thought, hooray! Morale:  ",
                         -2, "So I have {0} assignments to grade. Let's get started! - says {1}. Energy level: "
                       .format(len(assignments), mentor.nick_name))
else:
    event = Athomosphere(-3, "Oh god, this is a shitload of assignments to grade... Morale: ",
                         -3, "So I have {0} assignments to grade. Let's get started! - says {1}. Energy level: "
                       .format(len(assignments), mentor.nick_name))

mentor.process(event.process_event())
mentor.process(event.process_atmosphere())
codecool_bp.drink_coffee(40)
input("")
for i in assignments:
    event = Study(3, "At least this way we can practice Python as well. Skill level: ",
                  -3, "Grading is soooo tiring. Energy level: ",)
    event = Athomosphere(*i.get_grade(),
                         -3, "Grading is soooo tiring. Energy level: ")


# script mentors working on the assignment
codecool_bp.drink_coffee(40)
input("")
print("The mentors noticed that some students still need some extra help with understanding the material.")
print("They invite those students for private mentoring. No student left behind!")
# script private mentoring
input("")
print("The day is over, let's see how the situation changed since the morning.")

input("")
codecool_bp.sum_stats("evening")
codecool_bp.report_day(codecool_bp.stat_morning, codecool_bp.stat_evening)

# script evaluation of the day (sum of energy level, skill level, morale)
#    depending on the result:
#        perfect day: go to terrace opening party
#        shitty day: go home and work more
