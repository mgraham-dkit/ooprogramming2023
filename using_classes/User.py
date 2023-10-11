class User:
    username = ""
    password=""
    fName = ""
    lName = ""
    
    def display(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"First name: {self.fName}")
        print(f"Last name: {self.lName}")