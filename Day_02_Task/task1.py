# User Login Access Control Program

username = input("Enter username: ")
account_status = input("Enter account status (active/inactive): ").lower()

if username != "" and account_status == "active":
    print("Login successful. Welcome,", username)
else:
    print("Login denied. Please check your credentials or account status.")

username=input("Enter Username: ")
account_status=input("Enter Account Status (Active or Inactive):").lower()

if username != "" and account_status == "active":
    print("Login successful. Welcome,", username)
else:
    print("Login denied. Please check your credentials or account status.")
