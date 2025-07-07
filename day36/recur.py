def fun(count , end):
    #baseCondition
    if count == end:
        return
    
    # operations
    print(count)
    count += 1

    #recursive function call
    fun(count , end)

#main code

fun(1,5) # initial function call
