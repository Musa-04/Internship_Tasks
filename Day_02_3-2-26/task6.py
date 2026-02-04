users = ["admin", "staff", "intern"]
roles = ["admin", "user"]

username = input("Enter username: ")
role = input("Enter role: ")

if username in users and role in roles:
    print("Access granted")
else:
    print("Access denied")
