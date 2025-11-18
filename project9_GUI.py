import tkinter as tk

window = tk.Tk()
window.title("Budget Buddy")
window.geometry("840x500")
window.configure(bg="lightblue")


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


    income_button = tk.Button(window, text="Submit", bg="white", fg="black", command=income_submit)

    # Layout screen 2
    welcome_label.pack(pady=40)
    income_label.pack()
    income_entry.pack()
    income_button.pack()



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

