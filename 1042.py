entrada = input().split()
entradaAlterada = [0,0,0]

for l in range(3) :
    entradaAlterada[l] = int(entrada[l])

troca = 1
while troca :
    troca = 0
    for i in range(2) :
        if entradaAlterada[i] > entradaAlterada[i + 1] :
            aux = entradaAlterada[i + 1]
            entradaAlterada[i + 1] = entradaAlterada[i]
            entradaAlterada[i] = aux
            troca = 1

for j in range(0, 3) :
    print(entradaAlterada[j])
print()
for k in range(0, 3) :
    print(entrada[k])