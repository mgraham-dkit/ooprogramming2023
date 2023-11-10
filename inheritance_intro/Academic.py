from Person import Person
from Staff import Staff


class Academic(Staff):
    def __init__(self, name, id, address, start_date, dept, modules = [], timetable = []):
        super().__init__(name, id, address, start_date, dept)
        self.modules = modules
        self.timetable = timetable

    def display(self):
        print(
            f"Academic[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, dept={self.dept}, modules={self.modules}, timetable={self.timetable}")