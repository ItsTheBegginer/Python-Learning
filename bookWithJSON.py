import json
import os
book = []
if os.path.exists("contactBook.json"):
    pass
else:
    with open("contactBook.json","w") as f:
        json.dump(book,f)

def Create():
    contact = {
    "name" : None,
    "phone": None,
}
    name = input("Enter name of the contact:")
    while True:
        phone = input("Enter 10 digit phone number:")
        if len(phone)!=10:
            print("Enter valid number")
            
        elif phone  in [contact["phone"] for contact in book]:
            print("Contact already exists")
        else:
            break

            
        
    
    contact["name"] = name
    contact["phone"] = phone

    book.append(dict(contact))
    with open("contactBook.json","w") as f:
        json.dump(book,f)
    print("Contact added successfully")


def Read():
    check = None
    while True:
        search = input("Enter the phone number:")
        if len(search)!=10:
            print("Enter valid number")
        else:
            break 
    with open("contactBook.json","r") as f:
        data = json.load(f)
    for i in range(0,len(book)):
        if data[i]["phone"]==search:
            check = i
            print(data[i])
    if check == None:
        print("Contact does not exist")        
def Update():
    check = None
    search = input("Enter name to be update")
    for i in range(0,len(book)):
            if book[i]["name"]==search:
                check = i
                print(book[i])
    if check == None:
            print("Contact does not exist")
    else:
        
        task = int(input("what to update\n1.name\n2.Number"))
        match task:
            case 1:
                New = input("enter value to update")
                book[check]["name"]= New 
            case 2:
                while True:
                    New = input("enter number")
                    if len(New)!=10:
                        print("Enter valid number")
                    else:
                        break
                book[check]["phone"] = New
                print(book[check])
def Delete():
    check = None
    search = input("Enter name to be delete")
    for i in range(0,len(book)):
            if book[i]["name"]==search:
                check = i
                print(book[i])
    if check == None:
            print("Contact does not exist")
    else:
        del book[check]
        print("Contact deleted successfully")
task = 0
while task!= 5:
    print("\n\nChoose your action")
    task = int(input("1.Create Contact\n2.Search Contact\n3.Update Contact\n4.Delete\n5.Exit\n"))


    match task:
        case 1:
            Create()
        case 2:
            Read()
        case 3:
            Update()
        case 4:
            Delete()
