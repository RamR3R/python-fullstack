from abc import ABC , abstractmethod
class Vehicle(ABC): #interface

    @abstractmethod
    def start(self):
        print("Vehicle started")

    @abstractmethod
    def horn(self):
        print("bum bum bum")

class Bike(Vehicle):
    wheels = 2

    def start(self):
        print("Vrummmm")

class Car(Vehicle):
    wheels = 4

    def start(self):
        print("mmmmmmm")

bike1 = Bike()
car1 = Car()

car1.start()
bike1.start()
bike1.horn()
