from Person import Person

def display_person(p):
    print(f"First name of person = {p.fName}")
    print(f"Second name of person = {p.lName}")
    print(f"Age of person = {p.age}")
    if(p.leftie_status is True):
        print("person is a leftie!")
    else:
        print(f"{p.fName.upper()} {p.lName.upper()}")

# Create default person and display it
p1 = Person()
display_person(p1)
   
# Create default Person and customise with user input
p2 = Person()
user_fName = input("Please enter the Person's first name: ")
user_lName = input("Please enter the Person's last name: ")

# Validate the age data to make sure the age is >= 0
valid = False
while not valid:
    user_age = int(input("Please enter the Person's age (must be 0 or more): "))
    if user_age >= 0:
        valid = True

# Reset validity flag and use to validate left-handed status
valid = False
status = False
while not valid:
    user_leftie = input("Is the person left-handed? (True/False): ")
    # Check if the user entered True or False (in any caps format)
    if user_leftie.lower() == "true" or user_leftie.lower() == False:
        # If so, accept the data
        valid = True
        # Convert it to a bool for storage
        if user_leftie.lower() == "true":
            status = True
        else:
            status = False
            
# Set fields of second person
p2.fName = user_fName
p2.lName = user_lName
p2.age = user_age
p2.leftie_status = status

# Display second person's information
display_person(p2)
