lista= [1,2,3,4,5]
lista_animal = ["Arara", "Boi", "Cabrito", "Zebra"]
print("--- Exercicio de listas ---\n\n Segunda posição da lista animal: {}".format(lista_animal[1]))

soma = 0
print("Listagem de números:")
for x in lista:
    print(x)
    soma += x
print("soma dos números acima: {}".format(soma))

print("\n ------------------- \n Soma dos numeros usando 'SUM': {}".format(sum(lista)))
print("\n Maior dos numeros usando 'MAX': {}".format(max(lista)))
print("\n Menor dos numeros usando 'MIN': {}".format(min(lista)))
print("\n\n Ultimo na ordem alfabetica dos animais usando 'MAX': {}".format(max(lista_animal)))
print("\n\n Primeiro na ordem alfabetica dos animais usando 'MIN': {}".format(min(lista_animal)))

print("\n\n -------- CONDICIONAL e adição à lista---------")
animal=input("Lembre-se da letra maiuscula! Nome do animal: ")

if animal in lista_animal:
    print("{} existe na lista animal".format(animal))
else:
    print("{} NÃO existe na lista animal, mas será inserido".format(animal))
    lista_animal.append(animal)

#'pop' sempre retira o ultimo da lista quando não tem nenhuma posição indicada dentro do ()
#lista_animal.pop()
#print(lista_animal)

#utilizando o 'remove'
lista_animal.remove("Boi")

#NOVA LISTA 
#nova_lista = lista_animal * 3
#print(nova_lista)
print(lista_animal)

#sort() - lista em ordem alfabetica
lista_desordem = ["Yasmin", "Ana", "Fernanda", "Carolina"]
lista_desordem.sort()
print(lista_desordem)

#reverse() - lista em desordem alfabetica
lista_desordem.reverse()
print(lista_desordem)