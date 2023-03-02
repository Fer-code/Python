from Televisoes import Televisao
#from Calculator import Calculo
from Contador_palavras import contador_letras #pode importar classes e métodos tmb

if __name__ == '__main__':
    TV = Televisao()
    print(TV.ligada)
    TV.power()
    print(TV.ligada)

    lista = ['cachorro' , 'gato' , 'elefante']
    print(contador_letras(lista))

    #ca = Calculo(1,2)
    #print(ca.soma())
