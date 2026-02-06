class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt

    def get_balance(self):
        return self.__balance

acc = BankAccount(10000)
acc.deposit(2000)
acc.withdraw(3000)
print(acc.get_balance())
