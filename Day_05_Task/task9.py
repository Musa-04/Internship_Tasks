class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def validate(self, p):
        if p == self.__pin:
            print("Access Granted")
        else:
            print("Wrong PIN")

atm = ATM(1234)
atm.validate(1234)
