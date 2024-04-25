class Account:
    def __init__(self,name,acc_num,balance):
        self.name=name
        self.acc_num=acc_num
        self.bal=balance


def deposit(self,ammount):
    self.balance+=ammount
    print(f"{self.name} Deposited{ammount} $.Current balance is :{self.balance}")

def withdraw(self,ammount):
    if self.balance>=ammount:
        self.balance-=ammount
        print(f"{self.name} Withdrew{ammount} $.Current balance is:{self.balance}")

#  Inheritance
class Savings_Acc(Account):
    def __init__(self,name,acc_num,balance,intrest_rate):
        # Constructor of the Account class
        super().__init__(name,acc_num,balance)
        self.intrest_rate=intrest_rate

def add_intrest(self):
    intrest=self.balance*self.intrest_rate
    self.deposit(intrest)

    # Creating for objects for this class Templaate
    acc1=Account("Ankush Srivastava","31231","200000000")
    acc1.deposit(10000000)
    acc1.withdraw(500000)
    print()
    savings_acc=Savings_Acc("Ankush Srivastava","12434",12313,9090)
    savings_acc.deposit(31231231)
    savings_acc.add_intrest()
    savings_acc.withdraw(300000)
    