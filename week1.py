# this first line is just used to make the plots appear nicely in the notebook
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import time

def verify(func):
    for i in range(50):
        print(f'{i}: {func(i)}')


# 4 different implementations
def recursive_fib(n):
    if n == 0:
        return 0
    elif n < 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
    
def table_fib(n):
    table = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            table.append(table[i - 1] + table[i - 2])
    return table[n]

def last2_fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    else:
        for i in range(n - 1):
            c = a + b
            a = b
            b = c
    return b

def analytic_fib(n):
    phi = 0.5 * (1 + np.sqrt(5))
    return (phi ** n - (1 - phi) ** n) / (np.sqrt(5))
    
    
verify(analytic_fib)
verify(last2_fib)

def timeFib(func, n):
    start = time.time()
    print(func(n))
    end = time.time()
    return end-start

def benchmark(func, i):
    N = list(range(i))
    T = [timeFib(func, n) for n in N]
    plt.plot(N, T)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title(str(func))

benchmark(recursive_fib, 30)
benchmark(table_fib, 100)
benchmark(last2_fib, 100)