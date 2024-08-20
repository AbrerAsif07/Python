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
    print("6) Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc = int(input("Enter acc_no: "))
        name = input("Enter your name: ")
        acc_type = input("Enter account type: ")
        bra = input("ENter branch= ")
        x = Banking(acc, name, acc_type, bra)
        accounts.append(x)
        print(accounts)
