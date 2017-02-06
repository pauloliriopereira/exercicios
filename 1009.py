nome = str( input() )
salarioFixo = float( input() )
totalDeVendas = float( input() )

salario = salarioFixo + ( totalDeVendas * 0.15 )

print( "TOTAL = R$ %1.2f" % salario )