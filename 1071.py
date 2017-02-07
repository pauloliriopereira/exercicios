entrada1 = int(input())
entrada2 = int(input())
soma = 0

if entrada1 <= entrada2:
    inicio = entrada1
    fim = entrada2
else:
    inicio = entrada2
    fim = entrada1

for i in range(inicio, fim):
    if i % 2 == 1:
        soma += i
if inicio % 2 == 1:
    soma -= inicio

print(soma)