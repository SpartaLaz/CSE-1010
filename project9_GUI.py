import tkinter as tk

window = tk.Tk()
window.title("Budget Buddy")
window.geometry("840x500")
window.configure(bg="lightblue")
welcome_label = tk.Label(window, text="Welcome to Budget Buddy!", font=("Arial", 14, "bold"), bg="lightblue", fg="black")
name_label = tk.Label(window, text="Enter your name", font=("Arial", 14, "bold"), bg="lightblue", fg="black")

welcome_label.grid(row=0, column=15, columnspan=2, pady=2)
name_label.grid(row=2, column=0, padx=5, pady=5)
window.mainloop()

