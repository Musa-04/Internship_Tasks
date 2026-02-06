class User:
    def __init__(self, password):
        self.__password = password

    def set_password(self, new_pwd):
        self.__password = new_pwd

u = User("admin123")
u.set_password("newpass")
print("Password updated")
