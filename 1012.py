valores = input().split()
pi = 3.14159

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

areaDoTriangulo = (a * c) / 2
areaDoCirculo = pi * c * c
areaDoTrapezio = (c * (a + b)) / 2
areaDoQuadrado = b * b
areaDoRetangulo = a * b

print("TRIANGULO: %1.3f" % areaDoTriangulo)
print("CIRCULO: %1.3f" % areaDoCirculo)
print("TRAPEZIO: %1.3f" % areaDoTrapezio)
print("QUADRADO: %1.3f" % areaDoQuadrado)
print("RETANGULO: %1.3f" % areaDoRetangulo)