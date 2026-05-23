def login(username, password):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == username and p == password:
                    print("Login Successful")
                    return
        print("Invalid credentials")

    except FileNotFoundError:
        print("User file not found")

login("admin", "1234")
