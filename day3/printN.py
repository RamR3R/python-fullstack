def print_till_n(n):
    for i in range( 1, n+1 ):
        print(i , end=" ")
    print("")

#main code

x = int(input("Enter number : ")) #5
for i in range(1 , 6):
    print_till_n(i)