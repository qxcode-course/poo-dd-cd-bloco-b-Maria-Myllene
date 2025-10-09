class Roupa:
    def __init__ (self):
        self.__tamanho: str = ""
    
    def __str__(self):
        return f"size: ({self.__tamanho})"

    def setTamanho(self, tamanho: str) -> bool:
        if tamanho != "PP" and tamanho != "P" and tamanho != "M" and tamanho != "G" and tamanho != "GG" and tamanho != "XG":
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = tamanho
        

def main():
    roupa = Roupa()

    while True:
        line = input()
        args: list[str] = line.split(" ")
        print("$" + line)

        if args [0] == "end":
            break
        elif args [0] == "show":
            print(roupa)
        elif args [0] == "size":
            tamanho = args [1]
            roupa.setTamanho(tamanho)
        else:
            print("fail: comando invalido")
        
main()