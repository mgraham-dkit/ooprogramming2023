from Person import Person
from Staff import Staff


class NonAcademic(Staff):
    def __init__(self, name, id, address, start_date, dept, role, parttime=False):
        super().__init__(name, id, address, start_date, dept)
        self.parttime = parttime
        self.role = role

    def display(self):
        print(
            f"Staff[name={self.name}, id={self.id}, address={self.address}, start_date={self.start_date}, dept={self.dept}, parttime={self.parttime}, role={self.role}")

    def calc_wage(self):
        return super().calc_wage() * 1.1

    def __eq__(self, other):
        if not isinstance(other, NonAcademic):
            return NotImplemented

        if not super().__eq__(other):
            return False
        if self.role != other.role:
            return False
        if self.parttime != other.parttime:
            return False

        return True

    def __hash__(self):
        return hash((super(), self.parttime, self.role))
