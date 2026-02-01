from utils import validateAmount,validateName,prettyPrint
from storage.file import load_json,save_json
All = []
def AddExpense():
    expense = {
        "name" : None,
        "price" : None
    }
    
    expense["name"]= validateName()
    expense["price"] = validateAmount()   
    All.append(dict(expense))
    save_json(All)
    

def View():
    var =load_json()
    prettyPrint(var)
    

def Search():
    
    see = input("Enter name of expense to view:")
    for i in range(len(All)):
        if All[i]["name"] == see:
            check = True
            print(All[i])
    if check!=True:
            print("Expense not found") 

def ExitProgram():
    print("Exiting...")
