entrada = input().split()

x1 = float(entrada[0])
y1 = float(entrada[1])

if x1 == 0 and y1 == 0:
    print("Origem")
elif x1 > 0 and y1 > 0:
    print("Q1")
elif x1 < 0 and y1 > 0:
    print("Q2")
elif x1 < 0 and y1 < 0:
    print("Q3")
elif x1 > 0 and y1 < 0:
    print("Q4")
elif x1 == 0 and (0 > y1 or y1 > 0):
    print("Eixo Y")
elif y1 == 0 and (0 > x1 or x1 > 0):
    print("Eixo X")