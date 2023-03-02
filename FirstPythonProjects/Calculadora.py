class Calculo:
    a = int(input('Entre com o primeiro valor'))
    b = int(input('Entre com o segundo valor'))

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    resto = a % b

    print('\n SOMA: {}. \n SUBTRACAO: {}. \n MULTIPLICACAO {}. \n DIVISAO {}. \n RESTO {}. \n'.format(soma, subtracao, multiplicacao, divisao, resto))