file = open("contacts.txt" , "r")

# data = file.read()
# print(data)

# This code opens a file named "contacts.txt" in read mode, 
# reads its content, prints it to the console, and then closes the file.

data = file.readlines()
print(data)

file.close()


# file = open("contacts.txt" , "w")
# file.write("Ram is the Tech Trainer \n")
# file.write("Jas is the Tech Trainer")

# file = open("contacts.txt" , "a")
# file.write("Trainers and Students\n")
# file.write("Good bad ugly\n")