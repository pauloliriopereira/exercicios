valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in range(6):
    numNotas = valor // notas[i]
    print("%d nota(s) de R$ %1.2f" % (numNotas, float(notas[i])))
    valor -= (numNotas * notas[i])

print("MOEDAS:")
for i in range(6):
    numMoedas = (round(valor, 2) * 100) // (moedas[i] * 100)
    print("%d moeda(s) de R$ %1.2f" % (numMoedas, moedas[i]))
    valor -= (numMoedas * moedas[i])