
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def can_pay(self, amount):
        return 0 <= amount <= self.balance

    def pay(self, amount):
        if not self.can_pay(amount):
            return False

        self.balance -= amount
        return True
