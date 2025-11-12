
def calc_balance(income, expenses):
    return float(income) - float(expenses)



def financial_status(balance):
    if balance > 0:
        print("Great! You are saving money.")
    elif balance == 0:
        print("You are breaking even.")
    else:
        print("**WARNING** You are overspending!")