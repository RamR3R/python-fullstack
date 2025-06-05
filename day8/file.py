data = {
}

# file = open("./bvc.txt" , "r")
# # data = file.read()
# # line = file.readline()
# # line2 = file.readline()
# # x = file.readline()
# # y = file.readline()

# lines = file.readlines() # list of the lines in the file

# file.close()

# # print(lines)

# # file = open("./sample.txt" , "w")

# # file.write("AP is Andhra Pradesh\n")
# # file.write("TN is Tamil Nadu")

# # file.writelines([
# #     "AP is Andhra Pradesh\n",
# #     "TN is Tamil Nadu"
# # ])

# # file.close()

# file = open("./sample.txt" , "a")

# while True:
#     n = input("Enter present number : ")
#     file.writelines([
#         "89",
#         "72",
#         "43"
#     ])

# file.close()

file = open("./sample.txt", "a+")
name = input("Enter Name : ")
age = int(input("Enter Age : "))
file.write(f"Name : {name} , Age:{age}\n")

