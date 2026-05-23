# TASK 02: ATM WITHDRAWAL FUNCTION
# Requirements:
# - amount <= balance
# - amount multiple of 100
# - return updated balance

def withdraw(balance, amount):
    if amount <= balance and amount % 100 == 0:
        balance -= amount
        return balance
    else:
        return "Invalid withdrawal"

print(withdraw(10000, 2000))