entrada = input().split()

horaInicial = int(entrada[0])
horaFinal = int(entrada[1])

duracao = 0

if horaFinal <= horaInicial:
    duracao = horaFinal + 24 - horaInicial
    print("O JOGO DUROU %d HORA(S)" % duracao)
else:
    duracao = horaFinal - horaInicial
    print("O JOGO DUROU %d HORA(S)" % duracao)