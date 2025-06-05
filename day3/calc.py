#main code
# import arth
import arth as my  #named import
# from arth import add #import single function

number_1 = int(input())

while True:
    op = input()

    if op == "=":
        print("End of calculation result = ",number_1)
        break

    number_2 = int(input())
    
    if op == "+":
        number_1 = my.add(number_1 , number_2)
    elif op == "-":
        number_1 = my.sub(number_1 , number_2)
    elif op == "*":
        number_1 = my.mul(number_1 , number_2)
    elif op == "/":
        number_1 = my.div(number_1 , number_2)

    print(number_1)
