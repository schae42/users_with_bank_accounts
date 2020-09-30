
class User: 
    def __init__(self, name_input, email_input):
        self.name = name_input
        self.email = email_input
        # self.account_balance = 0
        self.account = BankAccount(account_name='', int_rate=0.004, balance=0)
    
    def make_deposit(self, amount, account_name):
        # self.account_balance += amount
        self.account.deposit(amount, account_name)
        return self

    def make_withdrawal(self, amount, account_name):
        self.account.withdraw(amount, account_name)
        return self

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.account_balance += amount
    #     return self

    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account.account_balance}")
        # print(f"User: {self.name}, {self.account.display_account_info()}")
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, account_name, int_rate=0.004, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance
        
    def deposit(self, amount, account_name):
        self.account_balance += amount
        return self

    def withdraw(self, amount, account_name):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Current {self.account_name} Balance: ${self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance * self.int_rate
        return self

#create instances of class User
madison = User("madison", "mhanberry@fakemail.nope")
cloud = User("cloud", "cgooksu@pawmail.nope")

#create instances of class BankAccount
checking = BankAccount('Checking',0.001)
savings = BankAccount('Savings',0.004)

madison.make_deposit(500,checking).make_deposit(500,'Checking').make_deposit(200,'Savings').make_withdrawal(250,'Checking').account.yield_interest()
madison.display_user_balance()
cloud.make_deposit(300,checking).make_deposit(150,savings).make_deposit(200,savings).make_withdrawal(50,checking).account.yield_interest()
cloud.display_user_balance()