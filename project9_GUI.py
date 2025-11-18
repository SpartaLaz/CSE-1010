import tkinter as tk

window = tk.Tk()
window.title("Budget Buddy")
window.geometry("840x500")
window.configure(bg="lightblue")
expense_obj = ""

#screen 2
def window2(name):
    welcome_label = tk.Label(window, text=f"Hey {name}, Welcome to Budget Buddy!", font=("Arial", 32, "bold"), bg="lightblue", fg="black")
    
    income_label = tk.Label(window, text="Please Enter your Monthly Income!", font=("Arial", 28, "bold"), bg="lightblue", fg="black")

    income_entry = tk.Entry(window, width=50, bg="white", fg="black")

    def income_submit():
        while True:
            income = income_entry.get()
            try:
                float(income)  
                break
            except ValueError:
                income_label.config(text="Please enter a valid number!", fg="red")
                return
        print("PLACEHOLDER INCOME IS", income)
        window_expense_type()

    income_button = tk.Button(window, text="Submit", bg="white", fg="black", command=income_submit)

    # Layout screen 2
    welcome_label.pack(pady=40)
    income_label.pack()
    income_entry.pack()
    income_button.pack()

#screen 3
def window_expense_type():
    #gets rid of all previous widgets without needing to call every singe one
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Enter an expense type that you want to add:", font=("Arial", 32, "bold"), bg="lightblue", fg="black")
    status_label = tk.Label(window, text="", font=("Arial", 28, "bold"), bg="lightblue", fg="black")
    type_entry = tk.Entry(window, width=50, bg="white", fg="black")

    def submit_type():
        global expense_obj
        type = type_entry.get().strip()

        if type == "":
            status_label.config(text="Entry type cannot be empty!", fg="red")
            return
    # store in the backend budget() method **delete this comment once this is finished please**
        expense_obj = type
            
        print("STORED EXPENSE TYPE =", type)

        #window 4
        window_expenses_nametype()

    button = tk.Button(window, text="Submit", command=submit_type)
    label.pack(pady=40)
    status_label.pack()
    type_entry.pack()
    button.pack()

def window_expenses_nametype():
    #lets the user enter as many items until they click the finish button
    for widget in window.winfo_children():
        widget.destroy()
    label = tk.Label(window, text=f"Adding expenses for {expense_obj}:", font=("Arial", 32, "bold"), bg="lightblue", fg="black")
    instruction = tk.Label(window, text="Add expenses in 'type price' format (e.g Milk 20)", font=("Arial", 28, "bold"), bg="lightblue", fg="black")
    status_label = tk.Label(window, text="", font=("Arial", 28, "bold"), bg="lightblue", fg="black")
    entry = tk.Entry(window, width=50, bg="white", fg="black")  

    def add():
        text = entry.get().strip()
        try:
            category, price = text.split()
            float(price)
        except:
            status_label.config(text="ENTER IN (TYPE COST) FORMAT", fg="red")
            return
        #add the stuff to the back end method add_expenses() **please delete after doing so**
        print("EXPENSES ADDED", category, price)
        entry.delete(0, "end")

    add_btn = tk.Button(window, text="Add Expense", command=add)

    label.pack(pady=30)
    instruction.pack()
    status_label.pack()
    entry.pack()
    add_btn.pack(padx=10)

    

welcome_label = tk.Label(window, text="Welcome to Budget Buddy!", font=("Arial", 40, "bold"), bg="lightblue", fg="black")

name_label = tk.Label(window, text="Enter your name:", font=("Arial", 30, "bold"), bg="lightblue", fg="black")

name_entry = tk.Entry(window, width=50, bg="white", fg="black")


def submit_name_next_window():
    name = name_entry.get()
    print("PLACEHOLDER NAME IS", name)
    # Destroy screen 1 widgets
    welcome_label.destroy()
    name_entry.destroy()
    name_label.destroy()
    submit_button.destroy()

    # Build screen 2
    window2(name)


submit_button = tk.Button(window, text="Submit", bg="lightblue", command=submit_name_next_window)

# Layout screen 1
welcome_label.pack(pady=40)
name_label.pack()
name_entry.pack()
submit_button.pack()



window.mainloop()



