class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount: float or int ) -> None:
        if amount < 0: raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float or int) -> None:
        if amount > self.__balance: raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self) -> float or int:
        return self.__balance