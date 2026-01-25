while True:
    try:
        i = int(input("How many expenses do you want to add?\n "))
        break
    except ValueError:
        print("Enter a number")
    except Exception:
        print("Something went wrong")
TotalAmt = 0
AllExpenses = []
for i in range(i):
    Expenses = {
        "name": None,    
        "amount":None,
        "category":None
        }
    
    print("Experimet Number " + str(i+1) )
    while True:
        try:
            Expenses["name"] = input("Enter  expense name: ")
            Expenses["amount"] = int(input("Enter expense amount: "))
            Expenses["category"] = (input("Enter expense category: "))
            break
        except ValueError:
            print("Enter a number")
    
    TotalAmt += Expenses["amount"]
    
    AllExpenses.append(dict(Expenses))               


print(AllExpenses)
print("Total Expense Amount: ", TotalAmt)
