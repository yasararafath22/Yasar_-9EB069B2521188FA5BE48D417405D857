class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        elif amount > self.__balance:
            return "Insufficient funds"
        else:
            return "Invalid withdrawal amount"

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__balance}"

# Example usage:
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("12345", "John Doe", 1000.0)

    # Check the initial balance
    print(account.display_balance())

    # Deposit money
    print(account.deposit(500))

    # Withdraw money
    print(account.withdraw(200))

    # Check the updated balance
    print(account.display_balance())