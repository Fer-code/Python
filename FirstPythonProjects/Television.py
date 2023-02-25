class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: #nao precisa colocar "==true" pq ele já vai fazer se a condição for verdadeira, se quiser ao contrario pode colocar if not
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1

televisao = Televisao()
print(televisao.ligada)

televisao.power()
print(televisao.ligada)

televisao.power()
print(televisao.ligada)

print(televisao.canal)
televisao.aumenta_canal()

print(televisao.canal)
televisao.diminui_canal()

print(televisao.canal)




