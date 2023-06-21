from gradient_descent.gradient_descent import speepest_descent
from math import inf


def barrier(func, cons, x0, r0, c, e=1e-5):
    xk = x0
    rk = r0
    k = 0

    def g_x(x):
        sum = 0.
        for g in cons:
            sum += 1/g(x)

        return sum

    P = lambda x, rk: - rk * g_x(x)
    f_t = lambda x, rk: func(x) + P(x, rk)
    F = lambda x: f_t(x, rk)

    p = inf
    while p > e:
        xmin, k1 = speepest_descent(F, xk, 0.0001, 0.0001, 100, 0.5)
        p = P(xmin, rk)

        for g in cons:
            if g(xmin) >= 0:
                flag = False
            else:
                flag = True

        print(f'Наиск. спуск {k1} шагов, X* = {xmin}, P(x*, rk) = {p}, rk = {rk}, xk = {xk}, k = {k}')

        if flag:
            rk /= c
            xk = xmin
        else:
            rk /= 2

        k += 1

    return xmin, func(xmin), k


if __name__ == '__main__':
    f = lambda x: 7*(x[0]**2) + x[1]**2 - x[0]*x[1] + x[0]
    cons = (lambda x: x[0] + x[1] - 2, )

    print(barrier(f, cons, (1, 2), 1, 10, e=0.001))
