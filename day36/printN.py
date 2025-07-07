def printer(n):
    #Base Condition
    if n == 0: return
    #operation
    print(n)
    # recursion call
    printer(n-1)

#main code 
printer(5)

