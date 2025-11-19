import tkinter as tk
from library.classes_9 import Budget  # Import the Budget class from your library folder

# Dictionary to store all created budget categories
all_budgets = {}

# Create the main window
window = tk.Tk()
window.title("Budget Buddy")
window.geometry("840x500")
window.configure(bg="lightblue")

expense_obj = ""  # Stores the current expense category name

# THE INCOME SCREEN 
def window2(name):
    # Greeting label using the name entered from the first screen
    welcome_label = tk.Label(window, text=f"Hey {name}, Welcome to Budget Buddy!",
                             font=("Arial", 32, "bold"), bg="lightblue", fg="black")
    
    # Ask for monthly income
    income_label = tk.Label(window, text="Please Enter your Monthly Income!",
                            font=("Arial", 28, "bold"), bg="lightblue", fg="black")

    income_entry = tk.Entry(window, width=50, bg="white", fg="black")

    # Function runs when user submits their income
    def income_submit():
        while True:
            income = income_entry.get()
            try:
                float(income)  # Validate income as a number
                break
            except ValueError:
                # If invalid show red warning text
                income_label.config(text="Please enter a valid number!", fg="red")
                return

        print("PLACEHOLDER INCOME IS ", income)
        window_expense_type()  # Move to next screen

    # Submit button
    income_button = tk.Button(window, text="Submit", bg="white", fg="black", command=income_submit)

    # Display items on the window
    welcome_label.pack(pady=40)
    income_label.pack()
    income_entry.pack()
    income_button.pack()


# CHOOSE EXPENSE CATEGORY SCREEN 
def window_expense_type():
    # Clears the window so the new screen can be shown
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Enter an expense type that you want to add:",
                     font=("Arial", 32, "bold"), bg="lightblue", fg="black")
    status_label = tk.Label(window, text="", font=("Arial", 28, "bold"),
                            bg="lightblue", fg="black")
    
    type_entry = tk.Entry(window, width=50, bg="white", fg="black")

    # Runs when the user inputs a category (like "Food")
    def submit_type():
        global expense_obj
        type = type_entry.get().strip()

        # Create a new Budget object for this category
        global budget_obj
        budget_obj = Budget(type)

        # Store it in dictionary so reports later can use it
        all_budgets[type] = budget_obj

        # If the field was empty - show error
        if type == "":
            status_label.config(text="Entry type cannot be empty!", fg="red")
            return
        
        # Save category name and move to next screen
        expense_obj = type
        print("STORED EXPENSE TYPE =", type)
        window_expenses_nametype()

    button = tk.Button(window, text="Submit", command=submit_type)

    label.pack(pady=40)
    status_label.pack()
    type_entry.pack()
    button.pack()


# ADD EXPENSES TO CATEGORY SCREEN 
def window_expenses_nametype():
    # Clear previous screen
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text=f"Adding expenses for {expense_obj}:",
                     font=("Arial", 32, "bold"), bg="lightblue", fg="black")

    instruction = tk.Label(window, 
        text="Add expenses in 'type price' format (e.g Milk 20)",
        font=("Arial", 28, "bold"), bg="lightblue", fg="black")

    status_label = tk.Label(window, text="", font=("Arial", 28, "bold"),
                            bg="lightblue", fg="black")

    entry = tk.Entry(window, width=50, bg="white", fg="black")

    # Adds the typed item + price to the budget object
    def add():
        text = entry.get().strip()

        try:
            category, price = text.split()
            float(price)  # Validate price
        except:
            status_label.config(text="ENTER IN (TYPE COST) FORMAT", fg="red")
            return
        
        # Store category + price in the Budget object
        budget_obj.categories.append(category)
        budget_obj.expenses.append(float(price))

        print("EXPENSES ADDED", category, price)

        entry.delete(0, "end")  # Clear the entry box

    add_btn = tk.Button(window, text="Add Expense", command=add)

    # Place widgets
    label.pack(pady=30)
    instruction.pack()
    status_label.pack()
    entry.pack()
    add_btn.pack(padx=10)

    # Button to go back and add a NEW category
    finish_btn = tk.Button(window, text="Finish Category and Add Another", 
                           command=window_expense_type)

    # Button to finish the entire program and show final report
    report_btn = tk.Button(window, text="Finish and View Report", 
                           command=window_final_report)

    finish_btn.pack(pady=5)
    report_btn.pack(pady=5)


# THE WELCOME SCREEN 
welcome_label = tk.Label(window, text="Welcome to Budget Buddy!",
                         font=("Arial", 40, "bold"), bg="lightblue", fg="black")

name_label = tk.Label(window, text="Enter your name:", font=("Arial", 30, "bold"),
                      bg="lightblue", fg="black")

name_entry = tk.Entry(window, width=50, bg="white", fg="black")

# When user hits submit then go to next window
def submit_name_next_window():
    name = name_entry.get()
    print("PLACEHOLDER NAME IS", name)

    # Remove welcome screen widgets
    welcome_label.destroy()
    name_entry.destroy()
    name_label.destroy()
    submit_button.destroy()

    # Move to income screen
    window2(name)

submit_button = tk.Button(window, text="Submit", bg="lightblue",
                          command=submit_name_next_window)


# THE FINAL REPORT SCREEN 
def window_final_report():
    # Clear all widgets
    for widget in window.winfo_children():
        widget.destroy()

    title = tk.Label(window, text="Your Budget Report",
                     font=("Arial", 40, "bold"), bg="lightblue", fg="black")
    title.pack(pady=20)

    # Text box where all expenses will be listed
    report_box = tk.Text(window, width=80, height=20, bg="white", fg="black")
    report_box.pack()

    report_box.insert(tk.END, "==== FULL BUDGET REPORT ====\n\n")
    total = 0

    # Loop through each Budget object and print its items
    # category_name = dictionary key (e.g. "Food")
    # obj = the actual Budget object (with categories + expenses inside)
    for category_name, obj in all_budgets.items():
        report_box.insert(tk.END, f"--- Expenses for {category_name} ---\n")

        # zip() pairs up each category name with its matching price
        for cat, price in zip(obj.categories, obj.expenses):
            report_box.insert(tk.END, f"{cat}: {price}\n")
            total += price


# STARTUP SCREEN PACK 
welcome_label.pack(pady=40)
name_label.pack()
name_entry.pack()
submit_button.pack()

# Start the GUI loop
window.mainloop()
