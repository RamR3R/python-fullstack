arr = [1,1,2]
k = 2
def generate(index , subset , subSum):
    if index == len(arr):
        if subSum == k:
            print(subset)
        return
    
    #take that element in index
    subset.append(arr[index])
    subSum += arr[index]
    generate(index + 1 , subset , subSum)
    subset.pop()
    subSum -= arr[index]

    #not take that element in index
    generate(index + 1 , subset , subSum)

string = "abc"
def subSetString(index, sub):
    if index == len(string):
        print(sub)
        return

    #take
    sub += string[index]
    subSetString(index + 1 , sub)
    #remove the added string
    sub = sub[0:-1]

    #not take
    subSetString(index + 1 , sub)

generate(0, []  , 0)