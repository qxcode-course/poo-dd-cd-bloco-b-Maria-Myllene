class Pessoa:
    def __init__ (self, nome: str, idade: int):
        self.__nome: str = nome
        self.__idade: int = idade
    
    def getAge (self):
        return self.__idade
    
    def getName (self):
        return self.__nome
    
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
class Moto:
    def __init__(self, potencia: int, tempo: int, pessoa: Pessoa):
        self.__potencia: int = 1
        self.__pessoa = None
        self.__tempo: int = 0

    def __str__(self):
        if self.__pessoa == None:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:(empty)"
        else:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:({self.__pessoa})"
        
    def inserir (self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True
    
    def init (self, potencia: int):
        self.__potencia = potencia
    
    def remover(self) -> Pessoa | None:
        if self.__pessoa == None:
            print ("fail: empty motorcycle")
            return None
        aux: Pessoa = self.__pessoa
        self.__pessoa = None
        print(aux)
    
    def buyTime(self, time: int):
        self.__tempo += time
    
    def drive(self, drive: int):
        if self.__tempo == 0:
            print("fail: buy time first")
        elif self.__pessoa == None:
            print("fail: empty motorcycle")
        elif self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
        elif self.__tempo < drive:
                print (f"fail: time finished after {self.__tempo} minutes")
                self.__tempo = 0
        else:
            self.__tempo -= drive

    def honk (self):
        buzina = "P" + ("e" * self.__potencia) + "m"
        print(buzina)
        

def main():
    moto = Moto(1, 0, "")

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa (nome, idade)
            moto.inserir(pessoa)
        elif args[0] == "init":
            potencia = int(args[1])
            moto.init(potencia)
        elif args[0] == "leave":
            moto.remover()
        elif args[0] == "buy":
            time = int(args[1])
            moto.buyTime(time)
        elif args[0] == "drive":
            drive = int(args[1])
            moto.drive(drive)
        elif args[0] == "honk":
            moto.honk()
        else: 
            print("fail: comando invalido")

main()
