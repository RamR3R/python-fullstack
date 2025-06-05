# Exception Handling

while True:
    try:
        # number1 = int(input())
        # number2 = int(input())
        # result = number1/number2
        file = open("./sample.txt" , "a")
        name = input("enter name: ")
        number = int(input("Enter number: "))
        file.write(f"{name} : {number}\n")

    except Exception as error:
        print(f"Error is {error}")
    else:
        print("Try is executed successfully")

    finally:
        file.close()
        print("OK bro end of program, bye!!")



# except ZeroDivisionError:
#     print(f"Zerodivision Error happend bro so sorry")
# except ValueError:
#     print(f"Value Error happend bro so sorry")


