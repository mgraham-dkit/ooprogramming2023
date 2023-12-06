import datetime as dt
class Person:
    date_format = "%d/%m/%Y"

    def __init__(self, name, id, address, start_date):
        self.name = name
        self.id = id
        self.address = address
        if isinstance(start_date, str):
            self.start_date = dt.datetime.strptime(start_date, Person.date_format)
        elif isinstance(start_date, dt.date):
            self.start_date = start_date
        else:
            self.start_date = dt.datetime.now()

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        if self.id != other.id:
            return False
        if self.name != other.name:
            return False
        if self.address != other.address:
            return False
        if self.start_date != other.start_date:
            return False

        return True

    def __hash__(self):
        return hash((self.id, self.name, self.address, self.start_date))

    def display(self):
        print(f"Person[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}]")


    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented

        if self.name < other.name:
            return True
        else:
            return False