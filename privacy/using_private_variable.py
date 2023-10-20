from User import User

user = User("grahamm", "password1", "Michelle")
user.display()
print(f"{user.fName}")
print(f"{user.lName}")
print(f"{user.username}")
print(f"{user.get_password()}")