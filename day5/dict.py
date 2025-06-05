student = {
    "name" : "Ram",
    "age" : 15,
    "marks" : [98, 97, 96],
    "present" : True
    # "avg" we need to add avg
}

# print(student["name"])
# print(student["age"])

# student["name"] = "Siva"

# print(student["name"])


# student["name"] = input()

sum = 0
for i in student["marks"]:
    sum += i

student["avg"] = sum / len(student["marks"])
print("before : ",student)
# for i in student:
#     print(f"{i} = {student[i]}")

student["name"] = None # delete a key

print("after" ,student)

