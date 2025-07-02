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

def operate(a,b,op):
    if op == "+": return a+b
    elif op == "-": return a-b
    elif op == "*": return a*b
    elif op == "/": return a/b
    else: return 0

def eval_exp(exp):
    stack = []

    for i in exp:
        if i != ")":
            stack.append(i)
        else:
            tempStack = []
            while stack[-1] != "(":
                tempStack.append(stack.pop())

            result = 0 + int(tempStack.pop())
            while len(tempStack):
                x = tempStack.pop()
                if not x.isdigit():
                    result = operate(result , int(tempStack[-1]) , x)
                    tempStack.pop()
            stack.pop()
            stack.append(result)
        print(stack)

    return stack[-1]



#main driver code

exp1 = "((((2+3)))))" #only with (
exp2 = "((2+3+3)+5+(2*3))"

print(eval_exp(exp2))

# print(check_valid(exp2))