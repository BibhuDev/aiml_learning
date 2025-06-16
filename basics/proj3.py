##contact book

contacts= []

def menu():
    print("Contact book:")
    print("1.Add contact")
    print("2.Delete contact")
    print("3.View all contacts")
    print("4.Search contacts")
    print("5.Exit")

while True:
    menu()
    choice= int(input("Enter task: "))

    if choice==1:
        name=input("Enter contact name: ")
        num= input("Enter contact number: ")
        contacts.append({"name": name, "number": num})
        print("Contact added")

    elif choice==2:
        contact_num= int(input("Enter the contact you want to delete: "))-1
        if not contacts:
            print("no contacts to be deleted")
        else:
            if 0<=contact_num<len(contacts):
                deleted= contacts.pop(contact_num)
                print("Successfully removes the contact: ", deleted)
            else:
                print("Invalid input!")
    
    elif choice==3:
        if not num:
            print("No contacts")
        else:
            for contact in contacts:
                print(contact)
            
    elif choice==4:
        search_name= input("Enter the contact name you want to search: ").lower()
        found= False
        for contact in contacts:
            if contact["name"].lower()==search_name:
                print("The contact you were looking for: ", contacts["name"]-contacts["num"])
                found= True
                break
            else:
                print("The contact you were searching for is not present in the list")

    elif choice==5:
        print("Exiting contact book!")
        break

    else:
        print("Enter invalid operation")
        