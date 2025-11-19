import tkinter as tk
from library.classes_9 import Budget   # Import your Budget class

# ===============================
# Create file automatically
# ===============================
open("expenses.txt", "a").close()

# Dictionary storing ALL Budget objects
all_budgets = {}

# Global variables SO FINAL PAGE CAN USE THEM
global_income = 0.0      # User's income
expense_obj = ""         # Current category name

# Main window configuration
window = tk.Tk()
window.title("Budget Buddy")
window.geometry("840x500")
window.configure(bg="lightblue")


# ==================================================
# Helper function — write expense into a text file
# ==================================================
def write_expense_to_file(category, item, price):
    with open("expenses.txt", "a") as f:
        f.write(f"{category},{item},{price}\n")


# ==================================================
# SCREEN 2 — Income Screen
# ==================================================
def window2(name):

    welcome_label = tk.Label(window, text=f"Hey {name}, Welcome to Budget Buddy!",
                             font=("Arial", 32, "bold"), bg="lightblue", fg="black")

    income_label = tk.Label(window, text="Please Enter your Monthly Income!",
                            font=("Arial", 28, "bold"), bg="lightblue", fg="black")

    income_entry = tk.Entry(window, width=50, bg="white", fg="black")

    def income_submit():
        global global_income

        while True:
            income = income_entry.get()
            try:
                global_income = float(income)   # STORE income
                break
            except ValueError:
                income_label.config(text="Please enter a valid number!", fg="red")
                return

        print("INCOME STORED:", global_income)
        window_expense_type()

    income_button = tk.Button(window, text="Submit", bg="white",
                              fg="black", command=income_submit)

    welcome_label.pack(pady=40)
    income_label.pack()
    income_entry.pack()
    income_button.pack()


# ==================================================
# SCREEN 3 — Choose Expense Category
# ==================================================
def window_expense_type():

    # Clear screen
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Enter an expense type you want to add:",
                     font=("Arial", 32, "bold"), bg="lightblue", fg="black")

    status_label = tk.Label(window, text="", font=("Arial", 25, "bold"),
                            bg="lightblue", fg="black")

    type_entry = tk.Entry(window, width=50, bg="white", fg="black")

    def submit_type():
        global expense_obj, budget_obj

        category_type = type_entry.get().strip()

        if category_type == "":
            status_label.config(text="Entry type cannot be empty!", fg="red")
            return

        budget_obj = Budget(category_type)
        all_budgets[category_type] = budget_obj

        expense_obj = category_type
        print("CATEGORY CREATED:", expense_obj)

        window_expenses_nametype()

    button = tk.Button(window, text="Submit", command=submit_type)

    label.pack(pady=40)
    status_label.pack()
    type_entry.pack()
    button.pack()


# ==================================================
# SCREEN 4 — Add Expenses to Category
# ==================================================
def window_expenses_nametype():

    # Clear
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text=f"Adding expenses for {expense_obj}:",
                     font=("Arial", 32, "bold"), bg="lightblue", fg="black")

    instruction = tk.Label(window,
        text="Add expenses in 'item price' format (e.g. Milk 20)",
        font=("Arial", 25, "bold"), bg="lightblue", fg="black")

    status_label = tk.Label(window, text="", font=("Arial", 25, "bold"),
                            bg="lightblue", fg="black")

    entry = tk.Entry(window, width=50, bg="white", fg="black")

    def add():
        text = entry.get().strip()

        try:
            item, price = text.split()
            float(price)
        except:
            status_label.config(text="ENTER IN (ITEM PRICE) FORMAT", fg="red")
            return

        budget_obj.categories.append(item)
        budget_obj.expenses.append(float(price))

        write_expense_to_file(expense_obj, item, price)

        print("EXPENSE ADDED:", item, price)
        entry.delete(0, "end")

    add_btn = tk.Button(window, text="Add Expense", command=add)

    label.pack(pady=30)
    instruction.pack()
    status_label.pack()
    entry.pack()
    add_btn.pack(pady=10)

    finish_btn = tk.Button(window, text="Finish Category and Add Another",
                           command=window_expense_type)

    report_btn = tk.Button(window, text="Finish and View Report",
                           command=window_final_report)

    finish_btn.pack(pady=5)
    report_btn.pack(pady=5)


# ==================================================
# SCREEN 1 — Welcome
# ==================================================
welcome_label = tk.Label(window, text="Welcome to Budget Buddy!",
                         font=("Arial", 40, "bold"), bg="lightblue", fg="black")

name_label = tk.Label(window, text="Enter your name:",
                      font=("Arial", 30, "bold"), bg="lightblue", fg="black")

name_entry = tk.Entry(window, width=50, bg="white", fg="black")


def submit_name_next_window():
    name = name_entry.get()
    print("USER NAME:", name)

    welcome_label.destroy()
    name_entry.destroy()
    name_label.destroy()
    submit_button.destroy()

    window2(name)


submit_button = tk.Button(window, text="Submit", bg="lightblue",
                          command=submit_name_next_window)

welcome_label.pack(pady=40)
name_label.pack()
name_entry.pack()
submit_button.pack()


# ==================================================
# FINAL REPORT SCREEN
# ==================================================
def window_final_report():

    # Clear screen
    for widget in window.winfo_children():
        widget.destroy()

    title = tk.Label(window, text="Your Budget Report",
                     font=("Arial", 40, "bold"), bg="lightblue", fg="black")
    title.pack(pady=20)

    report_box = tk.Text(window, width=80, height=20,
                         bg="white", fg="black")
    report_box.pack()

    report_box.insert(tk.END, "==== FULL BUDGET REPORT ====\n\n")

    total_expenses = 0

    for category_name, obj in all_budgets.items():
        report_box.insert(tk.END, f"--- {category_name} ---\n")

        for item, price in zip(obj.categories, obj.expenses):
            report_box.insert(tk.END, f"{item}: ${price}\n")
            total_expenses += price

    report_box.insert(tk.END, "\n===========================\n")
    report_box.insert(tk.END, f"Total Expenses: ${total_expenses}\n")
    report_box.insert(tk.END, f"Income: ${global_income}\n")

    savings = global_income - total_expenses
    report_box.insert(tk.END, f"Savings: ${savings}\n")

    if savings > 0:
        report_box.insert(tk.END, "\n🎉 You are saving money! Great job!\n")
    elif savings < 0:
        report_box.insert(tk.END, "\n⚠️ You are overspending! Try to adjust your budget.\n")
    else:
        report_box.insert(tk.END, "\nYou are breaking even.\n")


# Start GUI
window.mainloop()
