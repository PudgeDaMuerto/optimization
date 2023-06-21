from gradient_descent.gradient_descent import *


def fletcher_reeves(func, x0, e1, e2, m):
    flag = False
    k = 0
    xk = list(x0)
    func_grad = grad(func, xk)
    prev_func_grad = func_grad
    while norma(func_grad) >= e1 and k < m:
        func_grad = grad(func, xk)
        beta = (norma(func_grad) ** 2)/(norma(prev_func_grad) ** 2)
        if k != 0:
            d = vect_diff(mult_vector_by_number(beta, d), func_grad)
        else:
            d = mult_vector_by_number(-1, func_grad)

        tk = ravn_poisk(lambda t: func(vect_add(xk, mult_vector_by_number(t, d))), 0, 1)
        xk1 = vect_add(xk, mult_vector_by_number(tk, d))
        if norma(vect_diff(xk1, xk)) < e2 and abs(func(xk1) - func(xk)) < e2:
            if flag:
                return xk1, k
            flag = True
        else:
            flag = False

        k += 1
        xk = xk1
        prev_func_grad = func_grad

        print(f'Градиент: {func_grad} beta: {beta} tk: {tk} xk1: {xk1} k: {k}')

    return xk, k


if __name__ == '__main__':
    f = lambda x: 7 * (x[0] ** 2) + x[1] ** 2 - x[0] * x[1] + x[0]

    x, k = fletcher_reeves(f, (1, 2), 0.001, 0.001, 50)
    print(x, k)
    print(f(x))
