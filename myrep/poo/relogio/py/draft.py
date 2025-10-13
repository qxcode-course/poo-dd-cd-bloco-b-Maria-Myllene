class Tempo:
    def __init__ (self, hora: int, minuto: int, segundo: int):
        self.__hora: int = hora
        self.__min: int = minuto
        self.__seg: int = segundo
    
    def __str__ (self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}"
    
    def setHour (self, hora: int): 
        if hora > 23 or hora < 0:
            print("fail: hora invalida")
            return
        self.__hora = hora

    def setMinute (self, minuto: int):
        if minuto > 59 or minuto < 0:
            print("fail: minuto invalido")
            return
        self.__min = minuto

    def setSecond (self, segundo: int):
        if segundo > 59 or segundo < 0:
            print("fail: segundo invalido")
            return
        self.__seg = segundo
        
    def getHour (self):
        return self.__hora
    
    def getMinute (self):
        return self.__min
    
    def getSecond (self):
        return self.__seg
    
    def nextSecond (self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
        if self.__min > 59:
            self.__min = 0
            if self.__hora < 23:
                self.__hora += 1
        if self.__hora == 23:
            self.__hora = 0
    
    def horaInit
        

def main():
    relogio = Tempo(0, 0, 0)

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.setHour(hora)
            relogio.setMinute(minuto)
            relogio.setSecond(segundo)
        elif args [0] == "next":
            relogio.nextSecond()
        elif args [0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.setHour(hora)
            relogio.setMinute(minuto)
            relogio.setSecond(segundo)
            relogio.__init__(hora, minuto, segundo)
            if hora > 23 or hora < 0:
                hora = 0
        else:
            print("fail: comando invalido")
main()