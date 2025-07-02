
expression = "(((2)+(3)))"

stack = []
# for i in expression:
# for i in range(0, len(expression)):

for i in expression:
    # print("current i : ", i)
    if i == "(":
        stack.append(i)
    elif i == ")":
        stack.pop()
    else:
        continue
    # print(stack)

if len(stack) == 0:
    print("Valid exp")
else:
    print("Invalid exp")

