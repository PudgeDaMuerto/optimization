import math


def f(x):
    return x**2 + 4*x + 6


def sven(func, x0, t):
    xk = x0
    k = 0
    f1 = func(x0 - t)
    f2 = func(x0)
    f3 = func(x0 + t)

    if f1 >= f2 and f2 <= f3:
        a0 = x0 - t
        b0 = x0 + t
        return a0, b0

    elif f1 <= f2 and f3 <= f2:
        return 0

    else:
        if f1 >= f2 >= f3:
            delta = t
            a0 = x0
            xk = x0 + t

        elif f1 <= f2 <= f3:
            delta = -t
            b0 = xk
            xk = x0 - t
            k = 1

        xk1 = xk + (2 ** k) * delta

        while func(xk1) < func(xk):
            fxk1 = func(xk1)
            fxk = func(xk)
            if fxk1 < fxk and delta == t:
                a0 = xk
                k += 1

            elif fxk1 < fxk and delta == -t:
                b0 = xk
                k += 1

            xk = xk1
            xk1 = xk + (2 ** k) * delta

        if delta == t:
            b0 = xk1
        else:
            a0 = xk1

        return a0, b0


def uniform_search(func, x0, t, e=1e-5):
    a, b = sven(func, x0, t)
    print(f'a={a}, b={b}')
    x = list()
    n = int(abs(b - a)/e)
    min = math.inf
    for i in range(1, n+2):
        x.append((a + (i*(b-a)) / n))
        xk = func(x[i-1])
        if xk < min:
            min = xk
            x_min = x[i-1]
            k = i-1

    return x_min, f'Отрезок: [{x[k-1]} ; {x[k+1]}]', f"Погрешность: {(x[k+1] - x[k-1])/2}"


if __name__ == "__main__":
    res, s1, s2 = uniform_search(f, 0, 1, e=0.5)
    print(res, s1, s2, sep='\n')

