entrada1 = int(input())
entrada2 = int(input())
entrada3 = int(input())
entrada4 = int(input())
entrada5 = int(input())

numPar = 0
numImpar = 0
numPositivo = 0
numNegativo = 0

entrada = [entrada1, entrada2, entrada3, entrada4, entrada5]

for i in entrada:
    if i % 2 == 0:
        numPar += 1
    elif i % 2 == 1:
        numImpar += 1
    if i < 0:
        numNegativo += 1
    elif i > 0:
        numPositivo += 1

print("%d valor(es) par(es)" % numPar)
print("%d valor(es) impar(es)" % numImpar)
print("%d valor(es) positivo(s)" % numPositivo)
print("%d valor(es) negativo(s)" % numNegativo)
