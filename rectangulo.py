from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    def __init__(self, base=None, altura=None):
        FiguraGeometrica.__init__(self, ancho=base, alto=altura)

if __name__ == '__main__':
    r1 = Rectangulo(base=5, altura=6)
    print(r1)
    print(r1.area())