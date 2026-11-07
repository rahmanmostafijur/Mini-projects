from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, acc_holder, init_balance):
        self.name = acc_holder
        self.__balance = init_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
            return True
        return False

    def check_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass


class savings_account(BankAccount):
    def __init__(self, acc_holder, init_balance):
        super().__init__(acc_holder, init_balance)
        self.interest_rate = 0.05

    def calculate_interest(self):
        return self.check_balance() * self.interest_rate


class current_account(BankAccount):
    def __init__(self, acc_holder, init_balance):
        super().__init__(acc_holder, init_balance)
        self.interest_rate = 0.02

    def calculate_interest(self):
        return self.check_balance() * self.interest_rate


savings_acc = savings_account("Emon", 1000)
current_acc = current_account("Rahman", 2000)

print("Savings Interest:", savings_acc.calculate_interest())
print("Current Interest:", current_acc.calculate_interest())

savings_acc.deposit(500)
current_acc.withdraw(1000)

print("Savings Balance:", savings_acc.check_balance())
print("Current Balance:", current_acc.check_balance())

