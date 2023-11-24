from Person import Person
from Student import Student
from Staff import Staff
from Academic import Academic
from NonAcademic import NonAcademic
import random as rand

def display_people(people):
    print("*" * 20)
    for p in people:
        print("-" * 10)
        p.display()
    print("*" * 20)



p1 = Person("Helen", 1, "42 Wallaby Way, Sydney", "12/12/2017")
p2 = Person("Ross", 2, "42 Wallaby Way, Sydney", "12/02/2007")
p3 = Person("Carol", 3, "42 Wallaby Way, Sydney", "21/01/2019")
people = [p1, p2, p3]

#display_people(people)

s1 = Student("Rachel", 1, "42 Wallaby Way, Sydney", "04/12/1997", "Computing Systems and Operations", 1)
s2 = Student("Joy", 2, "1 Carnival Place, Sunnydale", "20/02/2016", "Computing", 3)
s3 = Student("Hope", 3, "27 Helter Skelter Drive, Sherman, Ohio", "11/05/2013", "Software Development", 4)

people.append(s1)
people.append(s2)
people.append(s3)
#rand.shuffle(people)

#display_people(people)

staff1 = Staff("Heim", 22, "Brightmoon, Silverlake", "14/03/2012", "Visual and Human-Centred Computing")
staff2 = Staff("Ron", 44, "Little Whinging", "31/07/1999", "Computing and Mathematics")
staff3 = Staff("Roy", 126, "Chelsea, Chelly", "14/10/2019", "Human Resources")

a1 = Academic("Caroline", 203, "Centre Parks, Swords", "07/05/2010", "Humanities", ['Business Studies', 'Accounting'])
na1 = NonAcademic("Breda", 101, "Albatross Lane", "11/09/2023", "Computing and Mathematics", "Admin", True)

people.append(staff1)
people.append(staff2)
people.append(staff3)
people.append(a1)
people.append(na1)

print(people)
display_people(people)

print("Hello")
student_counter = 0
person_counter = 0
for p in people:
    if isinstance(p, Person):
        person_counter += 1
    elif isinstance(p, Student):
        if p.course.lower() == "Computing Systems and Operations".lower():
            student_counter += 1

print(f"{student_counter} students were found in that course")
print(f"{person_counter} people were found")