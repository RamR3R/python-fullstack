# class Mobile:
#     brand = ""
#     model = ""

#     def __init__(self ,brand , model):
#         self.model = model
#         self.brand = brand


#     def power_on(self):
#         print("Powering On")



# # object_name = constructor()
# ram_mobile = Mobile("Apple" , "11")
# print(f"{ram_mobile.brand} {ram_mobile.model}")

# prasad_mobile = Mobile("Apple" , "16 pro max")
# print(f"{prasad_mobile.brand} {prasad_mobile.model}")

# prasad_mobile.power_on()


class Vehicle:
    brand = ""
    model = ""

    def start(self):
        print("Vehicle has started!!!!")


class Car(Vehicle): #className(parentClass name)
    
    wheels = 4

    def __init__(self , x , y):
        self.brand = x
        self.model = y
    
    def start(self):        #over rided the parent class method
        print("Car has Started")


class Bike(Vehicle):

    wheels = 2
    def start(self):
        print("bike is starting mama bro...!!!")



ram_car = Car("BMW" , "M3")
print(f"{ram_car.model} {ram_car.brand}")
ram_car.start()


ram_bike = Bike()
ram_bike.brand = "Kawasaki"
ram_bike.model = "Z800"
ram_bike.start()

class Human:
    hands = 2
    legs = 2

class Father(Human):
    anger = 100


class Mother(Human):
    beauty = 100

class Child(Father , Mother):
    name = ""

    def __init__(self , name):
        self.name = name

    def nature(self):
        print(f"anger = {self.anger} and beauty = {self.beauty}")


# prasad = Child("prasad")
# prasad.nature()



