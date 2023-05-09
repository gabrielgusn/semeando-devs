import math

class Ponto:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #metodos
    def imprime_ponto(self):
        print(f' x  y\n({self.x}, {self.y})')

    @staticmethod
    def distancia(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        d = dx**2 + dy**2
        return math.sqrt(d)


p1 = Ponto(2, 4)

# p1.x = 5
p1.y = 10

p1.imprime_ponto()

p2 = Ponto(3,9)
d = Ponto.distancia(p1, p2)
print("A distancia eh", d)