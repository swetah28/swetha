# oop_demonstration.py - Example of OOP with If Conditions

class BankAccount:
    """Class representing a simple bank account."""
    
    def __init__(self, account_holder, initial_balance=0):
        # Attributes (OOP Concept: Encapsulation)
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account created for {self.account_holder} with balance: ₹{self.balance}")

    def deposit(self, amount):
        """Method to deposit money with validation (If Condition)."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount! Amount must be greater than 0.")

    def withdraw(self, amount):
        """Method to withdraw money with multiple validations (If Conditions)."""
        # Condition 1: Check if withdraw amount is positive
        if amount <= 0:
            print("Invalid withdrawal amount!")
        # Condition 2: Check for sufficient balance
        elif amount > self.balance:
            print(f"Insufficient funds! You tried to withdraw ₹{amount}, but only have ₹{self.balance}.")
        # Condition 3: Successful withdrawal
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    def display_status(self):
        """Display account status."""
        print(f"--- Account Status ---")
        print(f"Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")
        if self.balance < 500:
            print("Warning: Low balance! Minimum ₹500 recommended.")
        else:
            print("Balance is healthy.")
        print("-" * 23)

# --- Main Program Execution (Object Usage) ---
if __name__ == "__main__":
    # 1. Creating Objects (Instances of the class)
    my_account = BankAccount("Swetha", 1000)
    
    # 2. Applying If Conditions through method calls
    print("\n--- Testing Transactions ---")
    
    # Successful deposit
    my_account.deposit(500)
    
    # Failed withdrawal (too much)
    my_account.withdraw(2000)
    
    # Successful withdrawal
    my_account.withdraw(800)
    
    # Negative deposit check
    my_account.deposit(-100)
    
    # 3. Final display with conditional warning
    print("")
    my_account.display_status()

    # Creating another object
    john_account = BankAccount("John Doe", 200)
    john_account.display_status()
