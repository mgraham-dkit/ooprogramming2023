class Address:
    house_label = "House name/number"
    line1 = "Line 1"
    line2 = "Line 2"
    line3 = "Line 3"
    city = "City"
    state = "State"
    postcode = "Postcode"
    country = "Country"

    '''
        Parameterised constructor that contains TWO optional parameters:
            line2 is given a default value of "Line 2" in the constructor signature
            line3 is given a default value of "Line 3" in the constructor signature
            
        When creating an instance of this class, the required fields (i.e. the parameters 
        without default values) must be supplied but the optional fields can be left out. 
        
        When an optional field is left out, the default value specified in the signature 
        is stored in the corresponding attribute
        
        When a value is supplied for an optional field, that value is stored in its
        corresponding attribute
    '''
    def __init__(self, house_label, line1, city, state, postcode, country, line2="Line 2", line3 = "Line 3"):
        self.house_label = house_label
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country

    def display(self):
        print(f"House label: {self.house_label}")
        print(f"Line1: {self.line1}")
        print(f"Line2: {self.line2}")
        print(f"Line3: {self.line3}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Postcode: {self.postcode}")
        print(f"Country: {self.country}")