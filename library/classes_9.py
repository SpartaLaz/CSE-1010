class Budget:

    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses = []
        self.categories = []

    
    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"How many {self.expense_type} expenses do you want to add? (Integers only) "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        
        print("Enter expenses in \"Type cost\" format. for e.g., Milk 10")
        for i in range(num_expenses):
            while True:
                try:
                    type, exp = input(f"Enter expense #{i + 1}:").split()
                    self.expenses.append(float(exp))
                    self.categories.append(type)
                    break
                except ValueError:
                    print("Invalid input format. Please enter in 'Type cost' format.")

    def get_expenses(self):
        total = sum(self.expenses)
        print(f"Total money spent on {self.expense_type} is: {total}")
        return total
    print()
    
    def get_expenses_list(self):
        print(f"Money you spent on {self.expense_type}: are:")
        for i in range(len(self.expenses)):
            print(f"{self.categories[i]}: {self.expenses[i]}")
            print()

    
