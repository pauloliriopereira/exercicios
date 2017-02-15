memo = {}
def fib(n):
    calls = n
    if calls in memo:
        return memo[calls]
    if n < 2:
        ans = n
    else:
        ans = fib(n - 1) + fib(n - 2)

    memo[calls] = ans
    return ans

memo2 = {}
def numCalls(n):
    calls = n
    if calls in memo2:
        return memo2[calls]
    if n == 0 or n == 1:
        ans = 1
    else:
        ans = numCalls(n - 1) + numCalls(n - 2) + 1
    memo2[calls] = ans
    return ans

def numeroDeCasos(entrada):
    for j in entradas:
        calls = fib(j)
        num_calls = numCalls(j)
        print("fib(%d) = %d calls = %d" % (j, num_calls - 1, calls))

nCasos = int(input())

entradas = []
for i in range(nCasos):
    entradas.insert(i, int(input()))

numeroDeCasos(entradas)