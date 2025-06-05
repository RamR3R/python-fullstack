#main code
import contact_functions as cf
contacts = {}
print("\tContacts App")
while True:
    try:
        print("Choices :")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Edit contact")
        print("6. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            cf.add_contact(contacts)
        elif choice == 2:
            cf.view_contacts(contacts)
        elif choice == 3:
            cf.delete_contact(contacts)
        elif choice == 4:
            cf.find_contact(contacts)
        elif choice == 5:
            cf.edit_contact(contacts)
        else:
            print("Ok bye thank you!!!")
            break
    except Exception as error:
        print(f"Error occured details below \n {error}")
    else:
        print("Operation Done")
    finally:
        print("\n<====Contacts App====>")

