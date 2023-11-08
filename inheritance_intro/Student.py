from Person import Person
class Student(Person):
    def __init__(self, name, id, address, start_date, course, year):
        super().__init__(name, id, address, start_date)
        self.course = course
        self.year = year

    def display(self):
        print(f"Student[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, course={self.course}, year={self.year}")