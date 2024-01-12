expenses = []
expense1 = {'amount': '5.00', 'category': 'Speedy Barcodes UPC', 'date': '10/11/2023', 'additional_info': '783495426400'}
expenses.append(expense1)
expense2 = {'amount': '86.09', 'category': 'Sample 1', 'date': '10/12/2023', 'additional_info': '189645091001024428'}
expenses.append(expense2)


def addExpense(amount, category, date, additional_info):
    expense = {'amount': amount, 'category': category, 'date': date, 'additional_info': additional_info}
    expenses.append(expense)

def removeExpense():
    while True:
        listExpenses()
        print("what expense would you like to remove")
        try:
            expenseToRemove = int(input(">"))
            del expenses[expenseToRemove]
        except:
            print("Invalid input. Please try again.")
        
def totalSoFar():
    cost = 0.00 
    for i in expenses:
        cost += float(i['amount'])
    print("$" + str(cost))


def printMenu():
    print("Please choose one of the following options")
    print("1. Add expense")
    print("2. Remove an expense")
    print("3. List all expenses")
    print("4. View total spending so far")


def listExpenses():
    print("\nHere is a list of your expenses")
    print("---------------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'], " - ", expense['date'], " - ", expense['additional_info'])
        counter += 1
    print("\n\n")

if __name__ == '__main__':
    while True:
        printMenu()
        optionSelected = input(">")

        if(optionSelected == 1):
            print("how much was this expense?")
            while True:
                try:
                    amountToAdd = input(">")
                    break
                except:
                    print("Invalid input. Please try again.")
            
            print("What category was this expense?")
            while True:
                try: 
                    categoryToAdd = input(">")
                    break
                except:
                    print("Invalid input. Please try again.")
            
            print("When was this expense created?")
            while True:
                try: 
                    dateToAdd = input(">")
                    break
                except:
                    print("Invalid input. Please try again.")
            
            print("Input addtional information")
            while True:
                try: 
                    addInfo = input(">")
                    break
                except:
                    print("Invalid input. Please try again.")

            addExpense(amountToAdd, categoryToAdd, dateToAdd, addInfo)
        elif(optionSelected == 2):
            removeExpense()
        elif(optionSelected == 3):
            listExpenses()
        elif(optionSelected == 4):
            totalSoFar()
        else:
            print("Invalid input. Please try again.")



