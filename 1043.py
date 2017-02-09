entradaInicial = input().split()
entradaAlterada = [0, 0, 0]

for l in range(3):
    entradaAlterada[l] = float(entradaInicial[l])
    entradaInicial[l] = float(entradaInicial[l])

troca = 1
while troca:
    troca = 0
    for i in range(2):
        if entradaAlterada[i] > entradaAlterada[i + 1]:
            aux = entradaAlterada[i + 1]
            entradaAlterada[i + 1] = entradaAlterada[i]
            entradaAlterada[i] = aux
            troca = 1

if entradaAlterada[2] >= entradaAlterada[1] + entradaAlterada[0]:
    area = ((entradaInicial[0] + entradaInicial[1]) * entradaInicial[2]) / 2
    print("Area = %1.1f" % area)
else:
    soma = 0
    for j in entradaAlterada:
        soma += j
    print("Perimetro = %1.1f" % soma)