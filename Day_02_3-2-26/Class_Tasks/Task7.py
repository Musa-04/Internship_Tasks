# Task 07: Even-Odd Transaction Checker
# Scenario: Check if transaction ID is even or odd

transaction_id = int(input("Enter transaction ID: "))

if transaction_id % 2 == 0:
    print("Transaction ID is Even")
else:
    print("Transaction ID is Odd")
