class Passenger:
    def __init__ (self, nome: str, dinheiro: int):
        self.__nome: str = nome
        self.__dinheiro: int = dinheiro
    
    def __str__ (self):
        return f"{self.__nome}:{self.__dinheiro}"
    
    def getDinheiro(self):
        return self.__dinheiro
    
    def setDinheiro(self, valor: int):
        self.__dinheiro = valor



class Driver:
    def __init__ (self, name: str, money: int):
        self.__name: str = name
        self.__money: int = money
    
    def __str__ (self):
        return f"{self.__name}:{self.__money}"
    
    def getMoney(self):
        return self.__money

    def setMoney(self, valor: int):
        self.__money = valor


class Moto:
    def __init__(self, driver: Driver, passager: Passenger):
        self.__driver = None
        self.__passager = None
        self.__custo: int = 0
    
    def __str__ (self):
        return f"Cost: {self.__custo}, Driver: {self.__driver}, Passenger: {self.__passager}"
    
    def setDriver (self, driver: Driver):
        self.__driver = driver
        return True
    
    def setPass (self, passenger: Passenger):
        self.__passager = passenger
        return True

    def drive (self, drive: int):
        self.__custo += drive
        
    def leavePass (self):
        aux = self.__passager
        if self.__passager.getDinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")
            aux.setDinheiro(0)
            self.__driver.setMoney(self.__driver.getMoney() + self.__custo)
        else:
            aux.setDinheiro(aux.getDinheiro() - self.__custo)
            self.__driver.setMoney(self.__driver.getMoney() + self.__custo)
        print(f"{aux} left")
        self.__passager = None
        self.__custo = 0
    

        

def main():
    motouber = Moto("", "")

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)
    
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(motouber)
        elif args[0] == "setDriver":
            name = args[1]
            money = int(args[2])
            moto = Driver (name, money)
            motouber.setDriver(moto)
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            pessoa = Passenger (nome, dinheiro)
            motouber.setPass(pessoa)
        elif args[0] == "drive":
            drive = int(args[1])
            motouber.drive(drive)
        elif args[0] == "leavePass":
            motouber.leavePass()
        else:
            print("fail: comando invalido")

main()