entrada = input().split()

horaInicial = int(entrada[0])
minutoInicial = int(entrada[1])
horaFinal = int(entrada[2])
minutoFinal = int(entrada[3])

duracaoHoras = 0
duracaoMinutos = 0

if horaFinal <= horaInicial:
    duracaoHoras = horaFinal + 24 - horaInicial
    if minutoFinal < minutoInicial:
        duracaoHoras -= 1
        duracaoMinutos = minutoFinal + 60 - minutoInicial
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracaoHoras, duracaoMinutos))
elif minutoFinal < minutoInicial:
    duracaoHoras = horaFinal - horaInicial - 1
    duracaoMinutos = minutoFinal + 60 - minutoInicial
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracaoHoras, duracaoMinutos))
else:
    duracaoHoras = horaFinal - horaInicial
    duracaoMinutos = minutoFinal - minutoInicial
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (duracaoHoras, duracaoMinutos))