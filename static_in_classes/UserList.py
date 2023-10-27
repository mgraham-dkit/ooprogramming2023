from User import User


class UserList:
    def __init__(self):
        self.users = []

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def check_available(self, username):
        result = self.get_user(username)
        if result is None:
            return False
        else:
            return True

    def validate_login(self, username, password):
        for user in self.users:
            if user.username == username and user.get_password() == password:
                return True
        return False

    def add_user(self, user):
        if self.check_available(user.username):
            users.append(user)
            return True
        else:
            return False

    def display(self):
        for user in self.users:
            user.display()