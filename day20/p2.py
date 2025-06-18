# list = input().split(" ")
# print(list)
# ram Raj Rachel Roy jam for single line inp

n = int(input()) #3 no.of user name
name_list = []

for i in range(n):
    name = input()
    name_list.append(name)

print(name_list)


keyword = input() # ra

filtered_list = []

for x in name_list:
    if keyword.lower() in x.lower(): #filter case-insensitively
        filtered_list.append(x)

print(filtered_list)