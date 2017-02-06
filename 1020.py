valorDias = int(input())

ano = valorDias // 365
valorDias -= (valorDias // 365) * 365

meses = valorDias // 30
valorDias -= (valorDias // 30) * 30

print("%d ano(s)" % ano)
print("%d mes(es)" % meses)
print("%d dia(s)" % valorDias)