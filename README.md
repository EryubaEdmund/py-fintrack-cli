# 🏦 Bank Account System

A simple console-based banking application built with Python, demonstrating core **Object-Oriented Programming (OOP)** principles.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Core Concepts](#core-concepts)
  - [Classes](#1-classes)
  - [Objects & Instantiation](#2-objects--instantiation)
  - [Attributes](#3-attributes)
  - [Methods](#4-methods)
  - [The `__init__` Constructor](#5-the-__init__-constructor)
  - [The `self` Parameter](#6-the-self-parameter)
  - [Encapsulation](#7-encapsulation)
  - [Conditional Logic](#8-conditional-logic)
  - [Control Flow – Loops & Break](#9-control-flow--loops--break)
  - [User Input & Type Conversion](#10-user-input--type-conversion)
  - [f-Strings (Formatted String Literals)](#11-f-strings-formatted-string-literals)
  - [The `main()` Function & Entry Point Guard](#12-the-main-function--entry-point-guard)
- [How to Run](#how-to-run)
- [Example Session](#example-session)
- [File Structure](#file-structure)

---

## Overview

This program simulates a basic bank account where a user can:

- 💰 **Deposit** money
- 💸 **Withdraw** money (with balance validation)
- 📊 **Check** their current balance
- 🚪 **Exit** the application

It is structured around a single class (`BankAccount`) and a `main()` driver function.

---

## Core Concepts

### 1. Classes

A **class** is a blueprint for creating objects. It defines the structure (attributes) and behavior (methods) that all instances of that class will share.

```python
class BankAccount:
    ...
```

Think of a class like a cookie cutter — it defines the shape, while each cookie (object) is a unique instance made from it.

---

### 2. Objects & Instantiation

An **object** is a specific instance of a class. **Instantiation** is the act of creating one.

```python
account = BankAccount(name)
```

Here, `account` is an object — a real, usable bank account created from the `BankAccount` blueprint. Each object has its own separate data.

---

### 3. Attributes

**Attributes** are variables that belong to an object. They store the object's state.

```python
self.owner = owner    # Stores the account holder's name
self.balance = balance  # Stores the current balance
```

| Attribute | Type | Purpose |
|---|---|---|
| `owner` | `str` | Name of the account holder |
| `balance` | `float` | Current money in the account |

---

### 4. Methods

**Methods** are functions defined inside a class. They describe what an object can *do*.

| Method | Description |
|---|---|
| `__init__()` | Initializes a new account with an owner and optional starting balance |
| `deposit(amount)` | Adds money to the balance if the amount is positive |
| `withdraw(amount)` | Deducts money if the amount is valid and funds are sufficient |
| `check_balance()` | Prints the current balance |

```python
account.deposit(500)      # Call the deposit method on the account object
account.check_balance()   # Call the check_balance method
```

---

### 5. The `__init__` Constructor

`__init__` is a **special (dunder) method** automatically called when a new object is created. It sets up the object's initial state.

```python
def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
```

- `owner` is a **required** parameter — you must supply a name.
- `balance=0` is an **optional** parameter with a **default value** of `0`, meaning a new account starts empty unless specified otherwise.

---

### 6. The `self` Parameter

`self` refers to the **current instance** of the class. It allows methods to access and modify the object's own attributes.

```python
def deposit(self, amount):
    self.balance += amount  # Updates THIS specific account's balance
```

Every method in a class must have `self` as its first parameter, though Python passes it automatically — you never include it when calling the method.

---

### 7. Encapsulation

**Encapsulation** means bundling data (attributes) and the logic that operates on it (methods) together inside a class, and controlling how that data is accessed or modified.

In this program, the balance is only ever changed through `deposit()` and `withdraw()` — both of which include validation logic:

```python
def withdraw(self, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > self.balance:
        print("Insufficient funds.")
    else:
        self.balance -= amount
```

This prevents invalid operations (e.g., withdrawing more than the balance) from corrupting the account's state.

---

### 8. Conditional Logic

`if / elif / else` statements control which code runs based on conditions.

```python
if amount > 0:
    self.balance += amount
    print(f"Deposited: {amount}")
else:
    print("Deposit amount must be positive.")
```

- `if` — checks the first condition
- `elif` — checks an additional condition if the previous ones were `False`
- `else` — runs when none of the above conditions are `True`

---

### 9. Control Flow – Loops & Break

A `while True` loop runs **indefinitely** until explicitly stopped. The `break` statement exits the loop.

```python
while True:
    choice = input("Enter choice (1-4): ")
    ...
    if choice == "4":
        print("Thank you for using the system.")
        break  # Exits the loop and ends the program
```

This pattern is common in menu-driven console applications.

---

### 10. User Input & Type Conversion

`input()` always returns a **string**. When a number is needed, it must be explicitly converted.

```python
amount = float(input("Enter amount to deposit: "))
```

| Function | Converts To |
|---|---|
| `int()` | Whole number (integer) |
| `float()` | Decimal number |
| `str()` | Text (string) |

---

### 11. f-Strings (Formatted String Literals)

**f-strings** let you embed variable values directly inside a string using `{}` placeholders.

```python
print(f"Deposited: {amount}")
print(f"Current balance: {self.balance}")
```

The `f` prefix before the quote tells Python to treat the string as a template and substitute the variable values at runtime.

---

### 12. The `main()` Function & Entry Point Guard

The `main()` function organizes the top-level application logic — gathering user input and calling methods on the account object.

```python
def main():
    name = input("Enter your name: ")
    account = BankAccount(name)
    ...
```

The entry point guard at the bottom ensures `main()` only runs when the file is executed **directly** — not when it is imported as a module by another script.

```python
if __name__ == "__main__":
    main()
```

This is a Python best practice for all script-based programs.

---

## How to Run

Make sure you have **Python 3** installed, then run:

```bash
python bank_account.py
```

---

## Example Session

```
=== Bank Account System ===
Enter your name: Alice

Choose an option:
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter choice (1-4): 1
Enter amount to deposit: 1000
Deposited: 1000.0

Enter choice (1-4): 2
Enter amount to withdraw: 250
Withdrawn: 250.0

Enter choice (1-4): 3
Current balance: 750.0

Enter choice (1-4): 4
Thank you for using the system.
```

---

## File Structure

```
bank_account.py
│
├── class BankAccount
│   ├── __init__(owner, balance=0)
│   ├── deposit(amount)
│   ├── withdraw(amount)
│   └── check_balance()
│
└── def main()
    └── if __name__ == "__main__"
```

---

*Created as a learning exercise in Python OOP fundamentals.*

## 📄 License
This project is licensed under the MIT License.
