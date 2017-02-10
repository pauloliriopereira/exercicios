def fib(n,num_calls):
    if n < 2:
        num_calls += 1
        return n, num_calls
    else:
        num_calls += 1
        return fib(n - 1) + fib(n - 2), num_calls

def numeroDeCasos(entrada):
    for j in entradas:
        calls, num_calls = fib(j,0)
        print("fib(%d) = %d calls = %d" % (j, num_calls - 1, calls))

nCasos = int(input())

entradas = []
for i in range(nCasos):
    entradas.insert(i, int(input()))

numeroDeCasos(nCasos)