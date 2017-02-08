entrada = input().split()

for l in range(3) :
    entrada[l] = float(entrada[l])

troca = 1
while troca :
    troca = 0
    for i in range(2) :
        if entrada[i] > entrada[i + 1] :
            aux = entrada[i + 1]
            entrada[i + 1] = entrada[i]
            entrada[i] = aux
            troca = 1

a = entrada[2]
b = entrada[1]
c = entrada[0]

if a >= b + c :
    print("NAO FORMA TRIANGULO")
else :
    if (a ** 2) == (b ** 2) + (c ** 2) :
        print("TRIANGULO RETANGULO")
    if (a ** 2) > (b ** 2) + (c ** 2) :
        print("TRIANGULO OBTUSANGULO")
    if  (a ** 2) < (b ** 2) + (c ** 2) :
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c :
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c :
        print("TRIANGULO ISOSCELES")