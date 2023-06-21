def f(x):
    return x**2 + 4*x + 6


def Fn(n):
    fib = list()
    fib.append(0), fib.append(1), fib.append(1)
    for i in range(3, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib


def fibonacci_method(a, b, l=1, e=1e-10):
    n = 1
    length = (b-a)/l
    fib = Fn(n)
    while fib[n] <= length:
        n += 1
        fib = Fn(n)

    z = (fib[n - 1] / fib[n]) * (b - a) + a
    y = a + b - z
    fy = f(y)
    fz = f(z)
    for k in range(n - 3):
        if fy <= fz:
            b = z
            z = y
            y = (fib[n - k - 3]/fib[n - k - 1]) * (b-a) + a
            fz = fy
            fy = f(y)
        else:
            a = y
            y = z
            z = (fib[n - k - 2]/fib[n - k - 1]) * (b - a) + a
            fy = fz
            fz = f(z)

    z = y + e
    if f(y) <= f(z):
        b = z
    else:
        a = y

    return (a + b)/2


def main():
    print(fibonacci_method(-4, 6, e=0.5))


if __name__ == '__main__':
    main()
