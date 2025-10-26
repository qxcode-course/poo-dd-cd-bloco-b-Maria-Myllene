class Lead:
    def __init__ (self, thicknessGraf: float, hardness: str, size: int):
        self.__thicknessGraf: float = thicknessGraf
        self.__hardness: str = hardness
        self.__size: int = size

    def __str__ (self):
        return f"[{self.__thicknessGraf}:{self.__hardness}:{self.__size}]"

    def getThickness (self):
        return self.__thicknessGraf
    
    def getHardness(self):
        return self.__hardness

    def getSize(self):
        return self.__size

    def setSize(self, tamanho: int):
        self.__size = tamanho
        return self.__size

class Pencil:
    def __init__(self, thickness: float, grafite: Lead):
        self.__thickness =  None
        self.__grafite = None

    def setInit (self, lapiseira: float):
        self.__thickness = lapiseira
        return True
    
    def __str__ (self):
        if self.__grafite == None:
            return f"calibre: {self.__thickness}, grafite: null"
        else:
            return f"calibre: {self.__thickness}, grafite: {self.__grafite}"
    
    def setInsert (self, grafite: Lead):
        if self.__thickness != grafite.getThickness():
            print("fail: calibre incompativel")
        elif self.__grafite != None:
            print("fail: ja existe grafite")
        else:
           self.__grafite = grafite
    
    def setRemove (self):
        if self.__grafite != None:
            self.__grafite = None
    
    def setWrite(self):
        if self.__grafite == None:
            print("fail: nao existe grafite")
        
        elif self.__grafite.getHardness() == "HB":
            if self.__grafite.getSize() == 10:
                print("fail: tamanho insuficiente")
            elif self.__grafite.getSize() - 1 < 10:
                self.__grafite.setSize(10)
                print("fail: folha incompleta")
            else:
                self.__grafite.setSize(self.__grafite.getSize() - 1)
        
        elif self.__grafite.getHardness() == "2B":
            if self.__grafite.getSize() == 10:
                print("fail: tamanho insuficiente")
            elif self.__grafite.getSize() - 2 < 10:
                self.__grafite.setSize(10)
                print("fail: folha incompleta")
            else:
                self.__grafite.setSize(self.__grafite.getSize() - 2)
        
        elif self.__grafite.getHardness() == "4B":
            if self.__grafite.getSize() == 10:
                print("fail: tamanho insuficiente")
            elif self.__grafite.getSize() - 4 < 10:
                self.__grafite.setSize(10)
                print("fail: folha incompleta")
            else:
                self.__grafite.setSize(self.__grafite.getSize() - 4)
        
        elif self.__grafite.getHardness() == "6B":
            if self.__grafite.getSize() == 10:
                print("fail: tamanho insuficiente")
            elif self.__grafite.getSize() - 6 < 10:
                self.__grafite.setSize(10)
                print("fail: folha incompleta")
            else:
                self.__grafite.setSize(self.__grafite.getSize() - 6)
        

def main():
    lapiseira = Pencil (0.0, "")

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "init":
            thickness = float(args[1])
            lapiseira.setInit(thickness)
        elif args [0] == "show":
            print(lapiseira)
        elif args [0] == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            grafite = Lead(thickness, hardness, size)
            lapiseira.setInsert(grafite)
        elif args [0] == "remove":
            lapiseira.setRemove()
        elif args [0] == "write":
            lapiseira.setWrite()
        else:
            print("fail: comando invalido")

main()