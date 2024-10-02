####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Hello {self.name}, your balance is {self.balance}'

    def owner(self):
        print(f'Account name : {self.name}')

    def balance(self):
        print(f'Your balance {self.balance()}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Sorry, you do not have enough')
        else:
            self.balance -= amount
            print(f'Withderaw Successful, your balance is {self.balance}')

    def deposit(self, add_balance):
        if add_balance < 0:
            print(f'Sorry cant add negative')
        else:
            self.balance += add_balance
            print(f'Your balance {self.balance} has been deposited')


# 1. Instantiate the class
acct1 = Account('Jose', 1000)

# 2. Print the object
print(repr(acct1))

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(100)

acct1.withdraw(150)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

# ## Good job!
