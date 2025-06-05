#functions
def add(dairy):
    name = input("enter name : ")
    mobile = int(input("Enter number : "))
    dairy[name] = mobile

def view_all_contacts(dairy):
    for key in dairy:
        print(f"{key} => {dairy[key]}")

def del_contact(dairy):
    del_name = input("Enter name to delete : ")
    del dairy[del_name]

def edit_contact(dairy):
    key = input("Enter the name to Edit : ")
    mobile = int(input("Enter the number to change : "))
    dairy[key] = mobile

def search_contact(dairy):
    query = input("Enter name to search : ")
    found = False
    for key in dairy:
        if query in key:
            print(f"{key} => {dairy[key]}")
            found = True
        
    if not found:
        print("Query not Found!!!")