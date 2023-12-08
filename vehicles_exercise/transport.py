class Vehicle:
    def __init__(self, make, colour, num_seats):
        self.make = make
        self.colour = colour
        self.num_seats = num_seats

    def __str__(self):
        return f"{self.make} in {self.colour} with {self.num_seats} seats"

    def __repr__(self):
        return f"Vehicle[make={self.make}, colour={self.colour}, num_seats={self.num_seats}]"

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False

        if self.make != other.make:
            return False
        if self.colour != other.colour:
            return False
        if self.num_seats != other.num_seats:
            return False

        return True

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __lt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        elif self.make == other.make:
            if self.colour < other.colour:
                return True
            else:
                return False
        elif self.make < other.make:
            return True
        else:
            return False

    def __gt__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        elif self.make == other.make:
            if self.colour > other.colour:
                return True
            else:
                return False
        elif self.make > other.make:
            return True
        else:
            return False

    def __le__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        elif self.make == other.make:
            if self.colour <= other.colour:
                return True
            else:
                return False
        elif self.make <= other.make:
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, Vehicle):
            return NotImplemented
        elif self.make == other.make:
            if self.colour >= other.colour:
                return True
            else:
                return False
        elif self.make >= other.make:
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self, model, engine_power, is_manual):
        self.model = model
        self.engine_power = engine_power
        self.is_manual = is_manual

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented

        if not super().__eq__(other):
            return False

        if self.model != other.model:
            return False
        if self.engine_power != other.engine_power:
            return False
        if self.is_manual != other.is_manual:
            return False

        return True

    def __ne__(self, other):
        return not self == other