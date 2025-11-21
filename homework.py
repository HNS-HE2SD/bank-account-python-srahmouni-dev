class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []  # list to store all client accounts
# Getters and setters for all attributes
    def get_CIN(self): return self.__CIN
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName
    def get_tel(self): return self.__tel
    def set_tel(self, tel): self.__tel = tel

    def add_account(self, acc):
        self.__accounts.append(acc) # method to add account to client's list

    def list_accounts(self):
        print(f"Accounts of {self.__firstName} {self.__lastName}:") 
        for acc in self.__accounts:
            print(f"Account {acc.get_code()} | Balance = {acc.get_balance()} DA") # print each account code and balance

    def display(self):
        print(f"CIN: {self.__CIN}, Name: {self.__firstName} {self.__lastName}, Tel: {self.__tel}")


class Account:
    __nbAccounts = 0 # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.__transactions = []          # list to store transaction history
        owner.add_account(self)           # link this account to the client

    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # credit
    def credit(self, amount, account=None):
        if amount <= 0:
            print("Amount must be positive.") # validation check
            return

        self.__balance += amount # increase balance

        if account is None:
            self.__transactions.append(f"Credited +{amount} DA") # record normal deposit
        else:
            self.__transactions.append(
                f"Received transfer +{amount} DA from Account {account.get_code()}" # record incoming transfer
            )

    # debit
    def debit(self, amount, account=None):
        if amount <= 0:
            print("Amount must be positive.") # prevent invalid amount
            return

        if self.__balance < amount:
            print("Insufficient balance.") 
            return

        self.__balance -= amount # subtract balance

        if account is None:
            self.__transactions.append(f"Debited -{amount} DA") # record normal debit
        else:
            self.__transactions.append(
                f"Transfer sent -{amount} DA to Account {account.get_code()}" # record outgoing transfer
            )

    # transfer
    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Amount must be positive.")
            return

        if self.__balance < amount:
            print("Insufficient balance for transfer.")
            return

        self.debit(amount, other_account) # debit sender
        other_account.credit(amount, self) # credit receiver

    # display
    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")

    # transactions history
    def displayTransactions(self):
        print(f"Transaction history for Account {self.__code}:")
        for t in self.__transactions:
            print("Transaction", t) # print each transaction

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)
