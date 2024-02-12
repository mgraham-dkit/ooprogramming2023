class Product:
    """
        Code for the Product class goes here
        Product has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
    """
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

class Book(Product):
    """
        Code for the Book class goes here
        Book has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
        an author
        one or more genres (these should be stored in a list)
    """