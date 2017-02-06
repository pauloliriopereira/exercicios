numFuncionario = int( input() )
numHorasTrabalhadas = int( input() )
valorHora = float( input() )

salario = numHorasTrabalhadas * valorHora

print( "NUMBER =", numFuncionario )
print( "SALARY = U$ %1.2f" % salario )