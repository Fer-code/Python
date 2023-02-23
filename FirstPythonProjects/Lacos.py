# a = int(input("Entre com um valor: "))
# div = 0

# for x in range(1, a+1):
#     resto = a%x
#     print(a,resto)
#     if resto ==0:
#         div = div + 1
#     #print(x)

# if div == 2:
#     print("O numero {} é primo".format(a))
# else:
#     print('O numero {} não é primo'.format(a))

#------------while
#nota = int(input("Entre com a nota: "))
#while nota > 10: 
#    nota = int(input('Nota inválida. Insira novamente: '))
#print(nota) - DEPOIS DE PASSAR PELO WHILE

print("------MÉDIA ANUAL-------")

notaA = int(input('Nota do primeiro bimestre: '))
while notaA > 10:
    notaA = int(input(('Nota do primeiro bimestre foi digitada incorretamente. Ajuste: ')))
notaB = int(input('Nota do segundo bimestre: '))
while notaB > 10:
    notaB = int(input(('Nota do segundo bimestre foi digitada incorretamente. Ajuste: ')))
notaC = int(input('Nota do terceiro bimestre: '))
while notaC > 10:
    notaC = int(input(('Nota do terceiro bimestre foi digitada incorretamente. Ajuste: ')))
notaD = int(input('Nota do quarto bimestre: '))
while notaD > 10:
    notaD = int(input(('Nota do quarto bimestre foi digitada incorretamente. Ajuste: ')))

media = (notaA + notaB + notaC + notaD)/4
print("A média anual é {}".format(media))