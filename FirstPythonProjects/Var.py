#---------------------------------------------------------
# a = int(input('Primeiro valor: '))
# b= int(input('Segundo valor: '))
# c= int(input('Terceiro valor: '))

# if a>b and a>c:
#     print('O maior número é {}'.format(a))
# elif b>a and b>c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa')


#---------------------------------------------------------
# d = int(input("Insira um número: "))
# resto=d % 2

# if resto==0:
#     print('O número é par')
# else:
#     print('O número é impar')


#---------------------------------------------------------
# e = int(input("Insira o primeiro número: "))
# f= int(input('Insira o segundo número: '))
# resto_e=e % 2
# resto_f=f %2

# if resto_e==0 or resto_f==0:
#     print('Existe número par')
# else:
#     print('Não foi digitado nenhum número par')


#---------------------------------------------------------
print("------MÉDIA ANUAL-------")

notaA = int(input('Nota do primeiro bimestre: '))
if notaA > 10:
    notaA = int(input(('Nota do primeiro bimestre foi digitada incorretamente. Ajuste: ')))
notaB = int(input('Nota do segundo bimestre: '))
if notaB > 10:
    notaB = int(input(('Nota do segundo bimestre foi digitada incorretamente. Ajuste: ')))
notaC = int(input('Nota do terceiro bimestre: '))
if notaC > 10:
    notaC = int(input(('Nota do terceiro bimestre foi digitada incorretamente. Ajuste: ')))
notaD = int(input('Nota do quarto bimestre: '))
if notaD > 10:
    notaD = int(input(('Nota do quarto bimestre foi digitada incorretamente. Ajuste: ')))

media = (notaA + notaB + notaC + notaD)/4
print("A média anual é {}".format(media))

