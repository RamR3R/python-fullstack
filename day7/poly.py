class Animal:
    def sound(self , sound):
        print(f"Animal sounding {sound}")
    def add(x , y):
        return x + y
    def add(x , y , z):
        return x + y + z
    # method overLoading

class Dog(Animal):

    def sound(self):
        print("Bow bow")    

class Cat(Animal):

    def sound(self):
        print("Meow meow")

class Parrot(Animal):

    def sound(self):
        print("Hi I'm speking")

    

list = [Dog() , Cat() , Parrot()]

for i in list:
    i.sound()