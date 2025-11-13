import os
from library.functions import calc_balance, financial_status
from library.classes_9 import Budget


os.system("cls")

while True:
     try:
         name = str(input("Enter your name:"))
         if any(ch.isdigit() for ch in name):
             print("Name cant contain numbers.")
         else:
             break
     except ValueError:
         print("Invalid input. Please enter a valid name.")

print()
print(f"Hey {name}, this is BudgetBuddy! Your personal Budgeting assisant")

while True:
    try:
        income = float(input("Enter your monthly income:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


grocery = Budget("Grocery")
car = Budget("Car")

grocery.add_expenses()
car.add_expenses()

grocery.get_expenses()
car.get_expenses()

bal = calc_balance(income, grocery.get_expenses() + car.get_expenses())

financial_status(bal)

grocery.get_expenses_list()
car.get_expenses_list()