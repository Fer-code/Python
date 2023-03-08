lista = [1, 10]

try:
    divisao = 10 / 0 
    #numero = lista[3]
    #x = a

    numero = lista[1]

except ZeroDivisionError:
    print("Não é possível dividir por 0.")
#except:
 #   print("Erro desconhecido")
except BaseException as ex:
    print("Erro desconhecido {}".format(ex))
    
#parte do código que depende que não tenha nenhum erro
else:
    print('Executa quando não ocorre exceção')

#vai executar de qualquer maneira
finally:
    print('Sempre executa')