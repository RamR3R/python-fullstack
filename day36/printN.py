def printer(n):
    #Base Condition
    if n == 0: return
    # recursion call
    printer(n-1)
    #operation
    print(n)

#main code 
printer(5)

