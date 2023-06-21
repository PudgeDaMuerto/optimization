from gradient_descent.gradient_descent import *
from newtons_method.matr_funcs import *
import numpy as np


def clone_and_add(vector, value, i):
    new_vector = dp(list(vector))
    new_vector[i] += value

    return new_vector


def second_derivative(func, x, fp, sp):
    delta = 0.00001
    x1 = clone_and_add(clone_and_add(x, delta, fp), delta, sp)
    x2 = clone_and_add(clone_and_add(x, delta, fp), -delta, sp)
    x3 = clone_and_add(clone_and_add(x, -delta, fp), delta, sp)
    x4 = clone_and_add(clone_and_add(x, -delta, fp), -delta, sp)

    return (func(x1) - func(x2) - func(x3) + func(x4)) / (4 * (delta ** 2))


def hessian_matr(func, x):
    res = []
    for i in range(len(x)):
        res.append([])
        for j in range(len(x)):
            res[i].append(second_derivative(func, x, i, j))

    return res


def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)


def newton(func, x0, e1, e2, m, t0):
    flag = False
    k = 0
    xk = list(x0)
    f_gradient = grad(func, xk)
    xk1 = xk
    while norma(f_gradient) > e1 and k < m:
        tk = t0
        f_gradient = grad(func, xk)

        print_matr(hessian_matr(func, xk))
        h_inv = inv_matr(hessian_matr(func, xk))
        if is_pos_def(np.matrix(h_inv)):
            d = multiply(matr_by_num(h_inv, -1), f_gradient)
        else:
            d = mult_vector_by_number(-1, f_gradient)

        while func(xk1) - func(xk) >= 0:
            xk1 = vect_add(xk, mult_vector_by_number(tk, d))
            tk = tk / 2

        if (norma(vect_diff(xk1, xk))) < e2 and abs(func(xk1) - func(xk)) < e2:
            if flag:
                return xk1, k
            flag = True
        else:
            flag = False

        xk = xk1
        k += 1

        print(f'Градиент: {f_gradient} d: {d} xk1: {xk1} k: {k}')

    return xk, k


if __name__ == '__main__':
    f = lambda x: 7 * (x[0] ** 2) + x[1] ** 2 - x[0] * x[1] + x[0]
    f1 = lambda x: ((x[0] + 2 * x[1] - 4) ** 4) + ((x[1] + 1) ** 2) + 7

    x, k = newton(f, (1, 2), 0.001, 0.001, 50, 0.5)
    print(x, k)
    print(f(x))
