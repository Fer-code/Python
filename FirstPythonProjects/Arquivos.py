def Escrever(texto):
    arquivo = open("teste.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def Atualizar(texto):
    arquivo = open("teste.txt", "a")
    arquivo.write(texto)
    arquivo.close()

def Ler(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read
    print(texto)

if __name__ == '__main__':
    #text = input('Gravar em arquivo: ')
    #Escrever(text)
    Ler('teste.txt')

