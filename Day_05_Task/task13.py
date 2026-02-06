class Account:
    def __init__(self, balance):
        self.balance = balance

class Savings(Account):
    def interest(self):
        return self.balance * 0.05

s = Savings(10000)
print(s.interest())
