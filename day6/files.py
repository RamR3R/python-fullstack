file = open("./sample.txt"  , "r")

data = file.read()
list_data = data.split("\n")

age_dict = {

}

for item in list_data:
    splitted_item = item.split(" ")
    age_dict[splitted_item[0]] = int(splitted_item[1])

print(age_dict) 



# names = file.readlines()

# file.write("kam")

# file.write("But the students feels different\n")
# file.writelines([
#                 "Then that's great\n" , 
#                 "Lets continue the class"
#                 ])

file.close()