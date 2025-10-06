class Chinela:
    def __init__ (self):
        self.__tamanho: int = 0
    
    def setTamanho (self, numeracao: int):
        if numeracao > 50 or numeracao < 20:
            print("Tamanho inválido! Limite: 20-50")
            return
        if numeracao % 2 == 1:
            print ("Valor inválido: digite uma numeração par.")
            return
        self.__tamanho = numeracao

    def getTamanho (self):
        return self.__tamanho

def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0:
        print("Digite o número da sua chinela")
        numeracao = int(input())
        chinela.setTamanho(numeracao)
    
    print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())

main()
    