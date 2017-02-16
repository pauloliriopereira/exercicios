entrada1 = input().split()

n1 = float(entrada1[0])
n2 = float(entrada1[1])
n3 = float(entrada1[2])
n4 = float(entrada1[3])

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
exame = 0

if 5.0 <= media <= 6.9:
    exame = float(input())

if 5.0 <= media <= 6.9:
    print("Media: %1.1f" % media)
    print("Aluno em exame.")
    print("Nota do exame: %1.1f" % exame)
    media = (media + exame) / 2
    if media >= 5.0:
        print("Aluno aprovado.")
    elif media < 4.9:
        print("Aluno reprovado.")
    print("Media final: %1.1f" % media)
elif media >= 7.0:
    print("Media: %1.1f" % media)
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: %1.1f" % media)
    print("Aluno reprovado.")