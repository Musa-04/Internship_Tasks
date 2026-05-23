class Payment:
    def pay(self, amt): pass

class UPI(Payment):
    def pay(self, amt): print("Paid via UPI")

class Cash(Payment):
    def pay(self, amt): print("Paid via Cash")

for p in [UPI(), Cash()]:
    p.pay(1000)
