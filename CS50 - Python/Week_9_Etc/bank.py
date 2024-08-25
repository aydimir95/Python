"""

balance = 0 # (2) removed this before 


def main():
    # balance = 0 # (1) still an error = cannot access local variable
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n): 
    # (0) there is a bug = unound local variable = to be able to change the global variable
    global balance
    balance += n

def withdraw(n):
    global balance # (3) this solves the problem using a global variable
    balance -= n


if __name__ == "__main__":
    main()
"""
# global = this is not a local variable this is actually a global, use it very carefully - there needs to be a notion to use it

class Account:
    def __init__(self):
        self._balance = 0

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter = Gives control
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()


# constants = cannot be changed

