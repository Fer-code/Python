class Error(Exception):
    pass

class InputError(Error): #colocando assim significa que vai herdar de erro
    def __init__ (self, message):
        self.message = message
        

while True: #enquanto verdade for verdade: ficará executando para sempre
    try:
        n = int(input('Insira um número de 0 a 10: '))
        print(n)

        if n > 10:
            #forçar uma exceção
            raise InputError('Nota não pode ser maior que dez')
        if n < 0:
            #forçar uma exceção
            raise InputError('Nota não pode ser menor que 0')
        break 
    except ValueError:
        print('O sistema só aceita números')
    except InputError as ex:
        print(ex)