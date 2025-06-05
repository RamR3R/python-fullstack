from abc import ABC , abstractmethod
class BankAccount(ABC):

    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def withdraw():
        pass

    @abstractmethod
    def deposit():
        pass

class SavingAccount(BankAccount):
    __balance = 0
    owner = "bank"

    def __init__(self , name , bal):
        self.owner = name
        self.__balance = bal

    def get_balance(self):
        print("balance = ",self.__balance)

class CurrentAccount:
    pass

a1 = SavingAccount("ram" , 500)
a1.get_balance()