def check_valid(exp):
    stack = []
    for i in exp:
        # print("current i : ", i)
        if i == "(" or i == "{" or i == "[" :
            stack.append(i)
        elif i == ")" or i == "}" or i == "]" :
            # print(i , " , " , stack[-1])
            if len(stack) != 0:
                if (i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or ( i == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return "Invalid"
            else:
                return "Invalid exp"
        else:
            continue
        
        print(i, " => " , stack)
    if len(stack) == 0:
        return("Valid exp")
    else:
        return("Invalid exp")


#main driver code

exp1 = "((((2+3)))))" #only with (
exp2 = "[{([2+3]*{6-1}*{5+4})}]"

print(eval_exp(exp2))

print(check_valid(exp2))