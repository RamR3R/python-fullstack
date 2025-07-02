def check_valid(exp):
    stack = []
    for i in exp:
        # print("current i : ", i)
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                return "Invalid exp"
        else:
            continue

    if len(stack) == 0:
        return("Valid exp")
    else:
        return("Invalid exp")


#main driver code

exp1 = "((((2+3)))))" #only with (
exp2 = "[{([2+3]{6-1{5+4})}]"

print(check_valid(exp2))