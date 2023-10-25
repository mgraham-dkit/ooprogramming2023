class User:
    # Create a static variable - this will belong to the class
    # as a whole
    user_count = 0
    def __init__(self, username, password, fName = None, lName = None):
        self.username = username
        self.__password = password
        self.fName = fName
        self.lName = lName
        # Increase the count of all users - this change will be shared by everyone
        User.user_count +=1
        # Save the updated count as the id for THIS User instance
        self.user_id = User.user_count

    def display(self):
        print(f"User[user_count={User.user_count}, user_id={self.user_id}, username={self.username}, password={self.__password}, fName={self.fName}, lName={self.lName}]")

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

    # Mark this as a class method
    # This will give the method access to all aspects of the class
    @classmethod
    # Takes cls (class) as the parameter, NOT self
    def reset_count(cls):
        # Refer to the variable as cls.user_count, NOT self.user_count
        cls.user_count = 0

    # Mark this as a static method
    # This has reduced access when compared to a class method
    # It's intended to only work with the data in this variable
    # and not mess with the class as a whole
    @staticmethod
    # Static methods take NO parameters (no self, no cls)
    def double_count():
        # Have to refer to the variable as class_name.variable
        # Can't use self or cls
        User.user_count *= 2