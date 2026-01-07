# 4.Simple Banking System (Console)
# Simulate bank accounts:
# create account
# deposit / withdraw
# transfer between accounts
# prevent negative balance


class Account:
    def __init__(self, account_number, balance) -> None:
        # validation
        if balance < 0:
            raise ValueError("Balance Can't be Negative.")

        self.account_number = account_number
        self._balance = balance

    # Dunder Methods
    def __str__(self) -> str:
        return f"Account Number: {self.account_number}, has balance: {self._balance} "

    # Instance Methods
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit can't be Negative or Zero")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw can't be Negative or Zero")
        self.balance -= amount

    @classmethod
    def transfer(cls, from_account, to_account, amount):
        if from_account.balance < amount:
            raise ValueError("Not Enough Balance")
        else:
            from_account.withdraw(amount)
            to_account.deposit(amount)


acc1 = Account(111, 1000)
acc2 = Account(222, 2000)
Account.transfer(acc1, acc2, 100)
print(acc1.balance)
print(acc2.balance)
