from Person import Person

person1 = Person("Albie", "D29992", "42 Wallaby Way", "10/12/2023")
person2 = Person("Benji", "D29991", "47 Wallaby Way", "10/12/2023")

if person1 < person2:
    print(f"{person1.name} comes before {person2.name}")
else:
    print(f"{person2.name} comes before {person1.name}")