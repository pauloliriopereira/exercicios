valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
#maior entre a e b
maior1 = (a + b + abs(a - b)) / 2

#maior entre maior1 e c
maior2 = (maior1 + c + abs(maior1 - c)) / 2

print("%d eh o maior" % maior2)