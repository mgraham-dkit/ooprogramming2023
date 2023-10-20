class User:
    def __init__(self, username, password, fName = None, lName = None):
        self.username = username
        self.__password = password
        self.fName = fName
        self.lName = lName

    def display(self):
        print(f"User[username={self.username}, password={self.__password}, fName={self.fName}, lName={self.lName}]")

    def change_password(self, new_pass):
        if len(new_pass) < 8:
            return False
        else:
            self.__password = new_pass
            return True

    def get_password(self):
        redacted = ""
        for char in self.__password:
            redacted += "*"

        return redacted