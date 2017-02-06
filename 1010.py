linha1 = input().split( " " )
linha2 = input().split( " " )


codPeca1, numPecas1, valorUnitarioDaPeca1 = linha1
codPeca2, numPecas2, valorUnitarioDaPeca2 = linha2

valorApagar = ( int(numPecas1) * float(valorUnitarioDaPeca1) ) + ( int(numPecas2) * float(valorUnitarioDaPeca2) )

print("VALOR A PAGAR: R$ %0.2f" % valorApagar)