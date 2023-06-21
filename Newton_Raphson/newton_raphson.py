from newtons_method.newton import *
import numpy as np


def newton_raphson(func, x0, e1, e2, m):
    flag = False
    k = 0
    xk = list(x0)
    f_gradient = grad(func, xk)
    while norma(f_gradient) > e1 and k < m:
        f_gradient = grad(func, xk)

        print_matr(hessian_matr(func, xk))
        h_inv = inv_matr(hessian_matr(func, xk))
        if is_pos_def(np.matrix(h_inv)):
            d = multiply(matr_by_num(h_inv, -1), f_gradient)
        else:
            d = mult_vector_by_number(-1, f_gradient)

        tk = ravn_poisk(lambda t: func(vect_add(xk, mult_vector_by_number(t, d))), 0, 1)
        xk1 = vect_add(xk, mult_vector_by_number(tk, d))

        if (norma(vect_diff(xk1, xk))) < e2 and abs(func(xk1) - func(xk)) < e2:
            if flag:
                return xk1, k
            flag = True
        else:
            flag = False

        xk = xk1
        k += 1
        print(f'Градиент: {f_gradient} d: {d} tk: {tk} xk1: {xk1} k: {k}')
    return xk, k


if __name__ == '__main__':
    f = lambda x: 7 * (x[0] ** 2) + x[1] ** 2 - x[0] * x[1] + x[0]
    f1 = lambda x: ((x[0] + 2 * x[1] - 4) ** 4) + ((x[1] + 1) ** 2) + 7

    x, k = newton_raphson(f1, (1, 2), 0.001, 0.001, 50)
    print(x, k)
    print(f(x))