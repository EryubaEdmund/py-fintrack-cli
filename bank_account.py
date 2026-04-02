# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:07:41 2026
@author: Socrates

bank_account.py

A simple console-based banking application using Object-Oriented Programming (OOP).
Users can deposit, withdraw, and check their account balance interactively.
"""


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        owner (str): Name of the account holder.
        balance (float): Current balance in the account.
    """

    def __init__(self, owner, balance=0):
        """
        Initialize a new BankAccount instance.

        Args:
            owner (str): The account holder's name.
            balance (float, optional): Starting balance. Defaults to 0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient balance exists.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        """
        Display the current account balance.

        Returns:
            None
        """
        print(f"Current balance: {self.balance}")


def main():
    """
    Main function to run the bank account application.

    Handles user input and interacts with the BankAccount object
    to perform operations such as deposit, withdrawal, and balance checking.
    """
    print("=== Bank Account System ===")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
    main()
