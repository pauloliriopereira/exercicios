entrada = int(input())
valorIn = 0
valorOut = 0

for i in range(entrada):
    valor = int(input())
    if 10 <= valor <= 20:
        valorIn += 1
    else:
        valorOut += 1

print("%d in" % valorIn)
print("%d out" % valorOut)