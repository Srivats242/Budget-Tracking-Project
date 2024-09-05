print("Welcome to the Budget Tracking App!")

username = input("Enter your username:")

print("Hi",username)

profession = input("Whats your profession: ")

try:
    Sourcesofincome = str(input("Enter your sources of income: "))
except ValueError:
    print("Enter valid sources of income")
    Sourcesofincome = str(input("Enter your sources of income: "))

try:
    income = float(input("Enter your income: "))
except ValueError:
    print("Please enter a valid amount")
    income = float(input("Enter your income: "))

Expenses =  {"Clothing" : 0, 
                "Groceries" : 0, 
                "Travel" : 0, 
                "Food" : 0, 
                "Vehicle Expenses" : 0,
                "Gym" : 0, 
                "Rent" : 0}

print("Available Expenses:")

for expense in Expenses:
    print(expense)

try:
    currentBudget = float(input("Enter your budget: "))
except ValueError:
    print("Please enter a valid budget amount")
    currentBudget = float(input("Enter your budget: "))


while True:
    Choiceofexpense = input("Choose expense(s) or enter exit to leave program: ")

    if Choiceofexpense.lower() == "exit":
        break

    if Choiceofexpense in Expenses:
        try:
            expenseamount = float(input("How much did you spend on " + Choiceofexpense + ":"))
        except ValueError:
            print("Please enter a valid amount")
            continue
        
        discounts = input("Have you recieved any discounts (yes or no)?")
        
        discountamount = 0


        if discounts == "yes":
            try:
                discountamount = float(input("Please enter a discount amount: " ))
            except ValueError:
                print("Please enter a valid discount amount")
                continue
        else:
            print("No discount, thats alright")
        

        totalcostwithdiscount = expenseamount - discountamount

        Expenses[Choiceofexpense] += totalcostwithdiscount

        currentBudget = currentBudget - totalcostwithdiscount


        print("Total Cost:", totalcostwithdiscount)

        print("Updated Budget:" + str(currentBudget))

    else:
        print("Invalid Expense category. Please choose an valid expense category from the list of expenses")
        break

print("Remaining Budget: ", currentBudget)