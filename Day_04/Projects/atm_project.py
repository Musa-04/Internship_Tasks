class InsufficientBalance(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalance("Insufficient balance")
    return balance - amount

try:
    bal = 10000
    bal = withdraw(bal, 2000)
    print("Remaining Balance:", bal)
except InsufficientBalance as e:
    print(e)
