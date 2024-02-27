class Product:
    def __init__(self, id_num, name, cost_price, retail_price, qty):
        self.id_num = id_num
        self.name = name

        if not isinstance(cost_price, int) and not isinstance(cost_price, float):
            raise TypeError("Product constructor: Inappropriate type provided for "
                            "cost_price (value must be numeric)")
        if cost_price < 0:
            raise ValueError("Product constructor: Inappropriate value provided for "
                             "cost_price (value must be >= 0)")
        self.cost_price = cost_price

        if not isinstance(retail_price, int) and not isinstance(retail_price, float):
            raise TypeError("Product constructor: Inappropriate type provided for "
                            "retail_price (value must be numeric)")
        if retail_price < 0:
            raise ValueError("Product constructor: Inappropriate value provided for "
                             "retail_price (value must be >= 0)")
        self.retail_price = retail_price

        if not isinstance(qty, int) and not isinstance(qty, float):
            raise TypeError("Product constructor: Inappropriate type provided for "
                            "qty (value must be numeric)")
        if qty < 0:
            raise ValueError("Product constructor: Inappropriate value provided for "
                             "qty (value must be >= 0)")
        self.qty = qty

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.id_num != other.id_num:
            return False
        return True

    def __str__(self):
        return f"{self.id_num}: {self.name} sells at {self.retail_price}."

    def __repr__(self):
        return (f"Product(id_num={self.id_num}, name={self.name}, cost_price={self.cost_price}, "
                f"retail_price={self.retail_price}, qty={self.qty})")

    def __hash__(self):
        return hash(self.id_num)

    def __format__(self, __format_spec):
        match __format_spec:
            case "short":
                return f"{self.id_num}: {self.name}"
            case "full":
                return (f"{self.id_num}: {self.name} costs {self.cost_price} and sells at {self.retail_price}. "
                        f"Quantity in stock: {self.qty}")
            case _:
                return self.__str__()

    def display(self):
        print("Product details:")
        print(f"\tID: {self.id_num}")
        print(f"\tCost price: {self.cost_price}")
        print(f"\tRetail price: {self.retail_price}")
        print(f"\tQuantity in stock: {self.qty}")
        print(f"\tName: {self.name}")

    def __lt__(self, other):
        if not isinstance(other, Product):
            return False

        return self.id_num < other.id_num

    def __le__(self, other):
        if not isinstance(other, Product):
            return False

        return self.id_num <= other.id_num

    def __gt__(self, other):
        if not isinstance(other, Product):
            return False

        return self.id_num > other.id_num

    def __gt__(self, other):
        if not isinstance(other, Product):
            return False

        return self.id_num >= other.id_num


class Book(Product):
    def __init__(self, id_num, name, cost_price, retail_price, qty, author, genres=None):
        super().__init__(id_num, name, cost_price, retail_price, qty)
        self.author = author
        if genres is None:
            self.genres = []
        else:
            self.genres = genres

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        if not super().__eq__(other):
            return False
        return True

    def __str__(self):
        return f"{self.id_num}: {self.name} sells at {self.retail_price}."

    def __repr__(self):
        return f"Book({super().__repr__()}, author={self.author}, genres={self.genres})"

    def __hash__(self):
        return hash(self.id_num)

    def __format__(self, __format_spec):
        match __format_spec:
            case "short":
                return f"{self.id_num}: {self.name} by {self.author}"
            case "full":
                return (f"{self.id_num}: {self.name} by {self.author} costs {self.cost_price} and sells at {self.retail_price}. "
                        f"Genres: {self.genres}. Quantity in stock: {self.qty}")
            case _:
                return self.__str__()

    def display(self):
        super().display()
        print(f"\tAuthor: {self.author}")
        print(f"\t\tGenre(s): {self.genres}")
