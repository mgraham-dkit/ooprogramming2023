from Person import Person


class Staff(Person):
    def __init__(self, name, id, address, start_date, dept):
        super().__init__(name, id, address, start_date)
        self.dept = dept

    def display(self):
        print(f"Staff[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, dept={self.dept}")