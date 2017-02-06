valor = int(input())

notas = [100, 50, 20, 10, 5, 2, 1]
print(valor)
for i in range(7):
    numNotas = valor // notas[i]
    print("%d nota(s) de R$ %d,00" % (numNotas, notas[i]))
    valor -= (numNotas * notas[i])