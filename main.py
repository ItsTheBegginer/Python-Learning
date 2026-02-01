from expenses import AddExpense 
from expenses import Search,View,ExitProgram
value = 0

while value!=4:
    try:
        value = int(input("Choose Option\n1.Add\n2.View\n3.Search\n4.Exit\n"))
    except ValueError:
          print("Enter a number")
          continue
    match value:
        case 1:
            AddExpense()
            
        case 2:
            View()
        case 3:
            Search()
        case 4:
            ExitProgram()
        case _:
            print("Invalid Option")