from Person import Person
from Student import Student
import random as rand

p1 = Person("Helen", 1, "42 Wallaby Way, Sydney", "12/12/2017")
p2 = Person("Ross", 2, "42 Wallaby Way, Sydney", "12/02/2007")
p3 = Person("Carol", 3, "42 Wallaby Way, Sydney", "21/01/2019")
people = [p1, p2, p3]

print("*"*20)
for p in people:
    print("-"*10)
    p.display()
print("*"*20)

s1 = Student("Rachel", 1, "42 Wallaby Way, Sydney", "04/12/1997", "Computing Systems and Operations", 1)
s2 = Student("Joy", 2, "1 Carnival Place, Sunnydale", "20/02/2016", "Computing", 3)
s3 = Student("Hope", 3, "27 Helter Skelter Drive, Sherman, Ohio", "11/05/2013", "Software Development", 4)

people.append(s1)
people.append(s2)
people.append(s3)
rand.shuffle(people)

print("*"*20)
for p in people:
    print("-"*10)
    if p.course == "Computing Systems and Operations":
        print(f"{p.name} is a CS&O student")
print("*"*20)