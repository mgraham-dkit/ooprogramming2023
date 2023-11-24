from Person import Person
import datetime as dt

class Staff(Person):
    def __init__(self, name, id, address, start_date, dept):
        super().__init__(name, id, address, start_date)
        self.dept = dept

    def display(self):
        print(f"Staff[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, dept={self.dept}")

    def calc_wage(self):
        now = dt.datetime.now()
        num_days = (now - self.start_date).days
        return num_days * 5

    def __repr__(self):
        return f"Staff[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, dept={self.dept}"