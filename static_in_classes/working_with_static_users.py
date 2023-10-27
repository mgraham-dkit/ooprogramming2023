from User import User
from UserList import UserList


u1 = User("grahamm", "password", "Michelle", "Graham")
u2 = User("bono", "Still haven't found", "Joe", "Bloggs")

u1.display()
u2.display()

User.reset_count()
u3 = User("bad_id", "shouldn't do this", "Bad Programmer", "Don't Hire")
print("-"*20)
u1.display()
u2.display()
u3.display()
User.double_count()
print("-"*20)
u1.display()
u2.display()
u3.display()

users = UserList()
users.add_user(u1)
users.add_user(u2)
users.add_user(u3)

users.display()