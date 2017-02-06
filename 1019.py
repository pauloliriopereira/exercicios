valorSeg = int(input())

hora = valorSeg // 3600
valorSeg -= (valorSeg // 3600) * 3600

minutos = valorSeg // 60
valorSeg -= (valorSeg // 60) * 60

segundos = valorSeg

print("{0}:{1}:{2}".format(hora, minutos, segundos))