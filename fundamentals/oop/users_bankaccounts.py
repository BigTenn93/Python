class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = .02, balance = 0):
        self.int = int_rate
        self.bal = balance
        if balance > 0:
            self.bal = balance
        BankAccount.all_accounts.append(self)

    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

    def deposit(self, amount):
        self.bal += amount
        return self

    def withdraw(self, amount):
        self.bal -= amount
        return self

    def display_account_info(self):
        print(f"Account balance is: ${self.bal}. Interest rate is: {self.int}%")
        return self

    def yield_interest(self):
        self.bal += round(self.bal * self.int)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

    def interest(self):
        self.account.yield_interest()
        return self

user1 = User("Tony", "iamironman@gmail.com")
user2 = User("Steve", "americasass@gmail.com")

user1.make_deposit(10000).make_deposit(2500).make_deposit(5000).make_withdrawal(1750).interest().display_balance()
user2.make_deposit(100).make_deposit(150).make_withdrawal(75).interest().display_balance()
print("----------------")
