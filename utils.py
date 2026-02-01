def validateAmount():
    while True:
        try:
            amount = int(input("Enter amount:"))
            break
        except ValueError:
            print("Enter a number")
            
    return amount
def validateName():
    while True:
        name = input("Enter name of the expense: ").strip()

        if name == "":
            print("❌ Name cannot be empty.")
        elif name.isdigit():  
            print("❌ Name cannot be only numbers.")
        else:
            return name
def prettyPrint(All):
    for expense in All:
        print(f"{expense}\n")
