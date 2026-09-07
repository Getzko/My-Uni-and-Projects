class BankAccount:
    bank_name="Bank abc"
    interest_rate=0.03
    account_count=0

    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        BankAccount.account_count+=1

    @property
    def isbalance(self):
        if self.balance < 0:
            print("you broke")
            raise ValueError("erorr")
        else: return self.balance

    @staticmethod
    def euros_to_dollars(euros):
        return euros * 1.17

    def display_in_dollars(self):
        dollars=self.euros_to_dollars(self.balance)
        print(f"Balance in euros:{self.balance}, dollars: {dollars}")

    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest

    def display_account(self):
        print(f"Name: {self.owner}, balance: {self.balance}, bank name: {self.bank_name} ")

bk1=BankAccount("jim",25)
bk1.display_account()
BankAccount.change_interest_rate(0.01)
bk1.add_interest()
bk1.display_in_dollars()
bk1.display_account()