class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Balance for {self.owner}: ${self.__balance}")

    def get_account_number(self):
      return self._account_number

    def set_account_number(self, new_account_number):
      self._account_number = new_account_number

    def _internal_check(self):
         print("Internal check performed.")

    def __secret_method(self):
      print("This is a secret method.")

account = BankAccount("135567153", "Hance", 10000)

account.deposit(500)
account.withdraw(200)
account.display_balance()
print()

account.deposit(300)
account.withdraw(1500)
account.display_balance()

print(f"Account number (using getter): {account.get_account_number()}")

account.set_account_number("987654321")
print(f"Account number (after setter): {account.get_account_number()}")

account._internal_check()