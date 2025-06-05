#function
def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    file = open("./contacts.txt" , "a")
    file.write(f"{name}:{mobile}\n")
    file.close()

def view_contacts(contacts):
    print("\n")
    file = open("./contacts.txt" , "r")
    data = file.readlines()
    print(data)
    for one_data in data:
        name , mobile = one_data.split(":")
        print(f"name : {name} , mobile :  {mobile}")

    file.close()

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    file = open("./contacts.txt" , "r")
    data = file.readlines()
    print(data)
    file.close()
    for i in range(len(data)):
        one_data = data[i]
        if name_to_delete == one_data.split(":")[0]:
            print("Deleted contact " , name_to_delete)
            data.pop(i)
            file = open("./contacts.txt" , "w")
            file.writelines(data)
            file.close()

def find_contact(contacts):
    query = input("Enter name to search : ")
    found = False
    file = open("./contacts.txt" , "r")
    data = file.readlines()
    for one_contact in data:
        name , mobile = one_contact.split(":")
        if query in name or query in mobile:
            print(f"Contact : {name} => {mobile}")
            found = True
    if not found:
        print("Query not Found!!!")

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)