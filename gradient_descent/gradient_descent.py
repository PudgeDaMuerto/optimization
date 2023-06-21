from copy import deepcopy as dp
from uniform_search.main import sven
import math


def derivative(func, x, i):
    x_delta = dp(list(x))
    x_delta[i] += 0.00001
    return (func(x_delta) - func(x)) / 0.00001


def grad(func, x):
    res = []
    for i in range(len(x)):
        res.append(derivative(func, x, i))
    return res


def norma(vector):
    sum = 0
    for el in vector:
        sum += el**2

    return sum ** 0.5


def mult_vector_by_number(num, vector):
    res = []
    for el in vector:
        res.append(num*el)
    return res


def vect_diff(v1, v2):
    res = []
    for el1, el2 in zip(v1, v2):
        res.append(el1 - el2)
    return res


def vect_add(v1, v2):
    res = []
    for el1, el2 in zip(v1, v2):
        res.append(el1 + el2)
    return res


def ravn_poisk(func, a0, t, e=1e-2):
    a, b = sven(func, a0, t)
    n = int((b-a)/e)
    min = math.inf
    for i in range(1, n+1):
        x = (a + (i*(b-a))/(n))
        xk = func(x)
        if xk < min:
            min = xk
            xmin = x

    return xmin


def speepest_descent(func, x0, e1, e2, m, t0):
    flag = False
    k = 0
    xk = list(x0)
    f_gradient = grad(func, xk)
    while norma(f_gradient) > e1 and k < m:
        tk = t0
        f_gradient = grad(func, xk)
        xk1 = vect_diff(xk, mult_vector_by_number(tk, f_gradient))
        while func(xk1) - func(xk) >= 0:
            tk = tk/2
            xk1 = vect_diff(xk, mult_vector_by_number(tk, f_gradient))

        if (norma(vect_diff(xk1, xk))) < e2 and abs(func(xk1) - func(xk)) < e2:
            if flag:
                return xk1, k
            flag = True
        else:
            flag = False

        xk = xk1
        k += 1
    return xk, k


def gradient_descent(func, x0, e1, e2, m):
    flag = False
    k = 0
    xk = list(x0)
    func_grad = grad(func, xk)
    while norma(func_grad) >= e1 and k < m:
        func_grad = grad(func, xk)
        tk = ravn_poisk(lambda t: func(vect_diff(xk, mult_vector_by_number(t, func_grad))), 0, 1, 0.001)
        xk1 = vect_diff(xk, mult_vector_by_number(tk, func_grad))
        if norma(vect_diff(xk1, xk)) < e2 and abs(func(xk1) - func(xk)) < e2:
            if flag:
                return xk1, k
            flag = True
        else:
            flag = False

        k += 1
        xk = xk1

    return xk, k


if __name__ == '__main__':
    f = lambda x: 7*(x[0]**2) + x[1]**2 - x[0]*x[1] + x[0]
    f1 = lambda x: ((x[0] + 2*x[1] - 4)**4) + ((x[1] + 1)**2) + 7

    print('Метод град. спуска с пост. шагом спуска:')
    print(gradient_descent(f1, (1, 2), 1e-5, 1e-5, 100))
    print('')
    print('Метод наискорешего спуска:')
    print(speepest_descent(f1, (1, 2), 1e-2, 1e-2, 100, 0.5))
