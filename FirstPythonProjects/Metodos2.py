class Calculadora:
    #def __init__(self):
        #pass # pq o init não pode ficar vazio

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b
    
    def sub (self, valor_a, valor_b):
        return valor_a - valor_b
    
    def mult (self, valor_a, valor_b):
        return valor_a * valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.sub(5, 3))
print(calculadora.mult(10,5))


