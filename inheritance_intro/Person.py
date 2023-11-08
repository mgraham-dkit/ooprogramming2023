class Person:
    def __init__(self, name, id, address, start_date):
        self.name = name
        self.id = id
        self.address = address
        self.start_date = start_date

    def display(self):
        print(f"Person[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}")