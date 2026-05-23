# Task 06: Role Verification System
# Scenario: Check if user role object is admin at execution time

admin_role = "admin"
user_role = input("Enter user role: ")

if user_role is admin_role:
    print("User has admin role")
else:
    print("User does not have admin role")
