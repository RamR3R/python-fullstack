#main code
import dairy_functions as df 
dairy = {
    "ram" : 909009090,
    "rocky" : 89898989
}

print(dairy)

while True:
    print("Choices : ")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Delete Contact")
    print("4. Edit Contact")
    print("5. Search")
    print("6. Exit")

    choice = int(input("Enter choice : "))

    if choice == 1:
        df.add(dairy)
    elif choice == 2:
        df.view_all_contacts(dairy)
    elif choice == 3:
        df.del_contact(dairy)
    elif choice == 4:
        df.edit_contact(dairy)
    elif choice == 5:
        df.search_contact(dairy)
    else:
        print("Exiting byee")
        break