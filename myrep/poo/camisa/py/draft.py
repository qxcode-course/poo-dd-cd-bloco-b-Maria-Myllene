class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def  getTamanho(self) -> str:
        return self.__tamanho 
    
    def setTamanho(self, valor: str) -> None:
        if valor != "PP" and valor != "P" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
            print("Tamanho inválido! Digite tamanho de roupa, meu parceiro!")
        else:
            self.__tamanho = valor
def main():
    camisa = Camisa()

    while camisa.getTamanho() == "":
        print("Digite o tamanho da sua camisa!")
        valor = input().upper()
        if camisa.setTamanho(valor) == True:
            break
    
    print("Parabéns, você comprou uma roupa tamanho", camisa.getTamanho())

main()
