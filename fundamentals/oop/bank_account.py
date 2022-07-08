class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int = int_rate
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount
        return self

    def withdraw(self, amount):
        if self.bal > amount:
            self.bal -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Account balance is: ${self.bal}.")

    def yield_interest(self):
        if self.bal > 0:
            self.bal += round(self.bal * self.int)
        else:
            print("Balance must be positive.")
        return self

Huntington = BankAccount(0.002, 2500)
USBank = BankAccount(0.0010, 800)

Huntington.deposit(100).deposit(200).deposit(300).withdraw(1500).yield_interest().display_account_info()
USBank.deposit(100).deposit(50).withdraw(25).withdraw(100).withdraw(50).withdraw(50).yield_interest().display_account_info()