import os

class Account:

    def __init__(self, filepath):
        with open(filepath,'r') as file:
            self.filepath=filepath #create an instance variable from parameter of init function
            self.balance = int(file.readlines()[-1])

    def withdraw (self, amount):
        self.balance=self.balance - amount
        self.commit()
    def deposit (self, amount):
        self.balance= self.balance + amount
        self.commit()
    def commit(self):
        with open(self.filepath,'a') as file:
            file.seek(0, os.SEEK_END)
            file.write(str(self.balance)+"\n")

class Current:
    # Class variables
    type = "current account"
    # Constructor method with instance variables fee
    def __init__(self,filename,fee):
        Account.__init__(self,filename)
        self.fee=fee
    # Method with instance variable amount
    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee
        Account.commit(self)
def main():
    # First object, set up instance variables of constructor method
    John_current=Current("John_account.txt",1)
    John_current.transfer(4)
    print(John_current.balance)

    Jane_current=Current("Jane_account.txt",1)
    Jane_current.transfer(4)
    print(Jane_current.balance)

if __name__ == "__main__":
    main()
