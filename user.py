class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private
        self.__transactions = []   # private list to track history

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited {amount} -> Balance: {self.__balance}")
            return "Amount deposited successfully"
        else:
            return "Invalid deposit"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal"
        elif self.__balance - amount < 0:
            return "Insufficient funds"
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew {amount} -> Balance: {self.__balance}")
            return "Amount withdrawn successfully"

    def get_balance(self):
        return self.__balance

    # 🚀 NEW METHOD
    def show_transactions(self):
        # TODO: print all transactions one by one
        if not self.__transactions:
            return "No transactions found."
        else:    
            for transaction in self.__transactions:
                print(transaction)


# 🔹 Test it
account = BankAccount("Alice", 100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))
print(account.deposit(680))
print(account.deposit(650))
print(account.deposit(550))
print(account.deposit(350))
print(account.deposit(250))
print(account.deposit(530))
print(account.deposit(530))
print(account.deposit(506))
print(account.deposit(500))
print(account.deposit(55320))
print(account.deposit(50))
print(account.withdraw(30))
print(account.withdraw(200))
print(account.deposit(680))
print(account.deposit(650))
print(account.deposit(550))
print(account.deposit(350))
print(account.deposit(506))
print(account.deposit(500))
print(account.deposit(55320))
print("Balance:", account.get_balance())

print("\nTransaction History:")
account.show_transactions()
