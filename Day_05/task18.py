class Admin:
    def login(self): print("Admin login")

class User:
    def login(self): print("User login")

for obj in [Admin(), User()]:
    obj.login()
