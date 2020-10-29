def fibonacciR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n <= 0:
        pass
    return fibonacciR(n-1) + fibonacciR(n-2)
for j in range(1,10):
    print(f"...................{j}")
    print('first', 'Second', "Fib_first", 'fib_sec', "ratio")
    for i in range(10,30):
        e = fibonacciR(i-j)
        f = fibonacciR(i)
        print(i-1, i, e, f, e/f)
