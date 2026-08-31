class BankAccount:
    def __init__(self, owner, account_number, balance = 0):
        self.owner=owner
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Balance: {self.balance}")
    def withdraw(self,amount):
        if amount <= 0:
            print("Cannot withdraw 0 or negative amounts")
        elif self.balance - amount < 0:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Balance: {self.balance}")
    def display_account(self):
        print(f"Name: {self.owner}, Acc nr: {self.account_number}, balance: {self.balance} ")

Acc1=BankAccount("John","321321")
Acc2=BankAccount("Marianne","876786687",2000)
Acc1.display_account()
Acc2.display_account()
print("Depositing 50 to John's account")
Acc1.deposit(50)
print("Withdrawing 100 from Marianne's account")
Acc2.withdraw(100)
print("Withdrawing 200 from johns acc")
Acc1.withdraw(200)
print("Withdrawing 0 from johns")
Acc1.withdraw(0)
