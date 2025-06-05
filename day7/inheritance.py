class Human: # base class or parent class
    hands = 2
    legs = 2

    def __init__(self , hand = hands , leg = legs):
        self.hands = hand
        self.legs = leg

    def eat(self):
        print("I'am Eating")

class Female(Human): # child or derived class
    gender = "female"

    def greet(self):
        print("Greeting from a female")

class Male(Human):
    gender = "male"

    def update_hands(self , handsCount):
        super().__init__(handsCount)
        
x = Male()
x.update_hands(4)
y = Female()
print(x.hands , " male")
print(y.hands , " Female")