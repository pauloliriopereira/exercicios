entrada = input().split()

codigo = int(entrada[0]) - 1
quantidade = int(entrada[1])

lista = [4.00, 4.50, 5.00, 2.00, 1.50]

total = lista[codigo] * quantidade
print("Total: R$ %1.2f" % total)