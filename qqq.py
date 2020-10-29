fibs = {}
def fib(n):
    if n <= 1:
        return n
    if n not in fibs:
        fibs[n] = fib(n-1) + fib(n-2)
    return fibs[n]


[fib(n) for n in range(10)]