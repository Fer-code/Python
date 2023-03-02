from datetime import date, time, datetime

def trabalhando_date():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))

    print(data_atual.strftime('%d %m %Y'))
    print(type(data_atual.strftime('%d %m %Y')))

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    print(horario.strftime('%H %M %S'))
    print(type(horario.strftime('%H %M %S')))

def trabalhando_datetime():
    dataatual = datetime.now()
    print(dataatual)

    print(dataatual.strftime('%d %m %Y %H %M %S'))
    print(dataatual.strftime('%c'))

    print(dataatual.day)
    print(dataatual.month)
    print(dataatual.year)
    print(dataatual.weekday())

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[dataatual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 23, 32)
    print(data_criada)
    print(data_criada.strftime('%c'))

    #conversão
    data_criada = '01/01/2001'
    data_convertida = datetime.strptime(data_criada, '%d/%m/%Y')
    print(data_convertida)



if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()
