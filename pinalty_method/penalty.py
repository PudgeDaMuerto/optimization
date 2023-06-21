from gradient_descent.gradient_descent import speepest_descent
from math import inf


def penalty(func, cons, x0, r0, c, e=1e-5):
    xk = x0
    rk = r0
    k = 0

    def g_plus_x(x):
        sum = 0
        for g in cons:
            if g['type'] == '>':
                sum += g['func'](x)**2

        return sum

    def g_x(x):
        sum = 0
        for g in cons:
            if g['type'] == '=':
                sum += g['func'](x)**2

        return sum

    P = lambda x, rk: (rk / 2) * (g_x(x) + g_plus_x(x))
    f_t = lambda x, rk: func(x) + P(x, rk)
    F = lambda x: f_t(x, rk)

    p = inf
    while p > e:
        xmin, k1 = speepest_descent(F, xk, 0.0001, 0.0001, 100, 0.5)
        p = P(xmin, rk)

        rk *= c
        xk = xmin
        k += 1

        print(f'Наиск. спуск {k1} шагов, X* = {xmin}, P(x*, rk) = {p}, rk = {rk}, xk = {xk}, k = {k}')

    return xmin, func(xmin), k


if __name__ == '__main__':
    f = lambda x: 7*(x[0]**2) + x[1]**2 - x[0]*x[1] + x[0]
    g = lambda x: x[0] + x[1] - 2

    cons = ({'type': '=', 'func': g},)
    print(penalty(f, cons, (1000, 2000), 1, 4, e=0.001))
