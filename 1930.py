valores = input().split()

soma = 0

for i in range(3):
    soma += int(valores[i]) - 1

soma += int(valores[3])

print(soma)
