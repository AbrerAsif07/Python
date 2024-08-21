"""
Banking:
     Attributes:acc_no, name, acc_type,branch
     Methods: display()
A banking system has attributes as shown in menu:
1. Add a account
    acc_no= int
    name=str
    acc_type=str
    balance=show default value
    branch=str
    x= banking(acc_no, name, acc_type, branch)
2. Display all account
3. Exit
"""

from typing import List


class Banking:
    def __init__(self, acc_no=int, name=str, acc_type=str, branch=str):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.branch = branch
        self.balance = 0

    def getBalance(self) -> int:
        return self.balance

    def deposit(self, amount) -> int:
        self.balance += amount

    def withdraw(self, amt):
        self.balance -= amt

    def display(self):
        print(f"acc_no = {self.acc_no}")
        print(f"Name = {self.name}")
        print(f"acc_type = {self.acc_type}")
        print(f"branch = {self.branch}")
        print(f"balance = {self.balance}")


accounts: List[Banking] = []

while True:
    print("1) Add account details")
    print("2) Display all account details")
    print("3) Check balance of an account")
    print("4) Deposit balance")
    print("5) Withdraw money")
    print("6) Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc = int(input("Enter acc_no: "))
        name = input("Enter your name: ")
        acc_type = input("Enter account type: ")
        bra = input("ENter branch= ")
        x = Banking(acc, name, acc_type, bra)
        accounts.append(x)

    elif choice == 2:
        for acc in accounts:
            acc.display()

    elif choice == 3:
        bl_show = int(input("enter acc no whose balance u want to check = "))
        for acc in accounts:
            if acc.acc_no == bl_show:
                print(f"Your balance is = {acc.getBalance()}")
            else:
                print("no such accounts")

    elif choice == 4:
        bl = int(input("enter acc no where you want to deposit = "))
        b2 = int(input("Enter amount you wish to deposit = "))
        for acc in accounts:
            if acc.acc_no == bl:
                acc.deposit(b2)
                print("your money has been deposited successfully")
            else:
                print("no such accounts")

    elif choice == 5:
        bl = int(input("enter acc no where you want to withdraw = "))
        b2 = int(input("Enter amount you wish to withdraw = "))
        for acc in accounts:
            if acc.acc_no == bl:
                acc.withdraw(b2)
                print("your money has been wuthdrawn successfully")
            else:
                print("no such accounts")

    elif choice == 6:
        break
    else:
        print("invalid input")
