def f(x):
    return x**2 + 4*x + 6


def half_division(func, ak, bk, xk, e):
    l = 2*e
    l2k = abs(bk-ak)
    while l2k > l:
        yk = ak + l2k / 4
        zk = bk - l2k/4
        if func(yk) < func(zk):
            return half_division(func, ak, xk, yk, e)
        elif func(zk) < func(xk):
            return half_division(func, xk, bk, zk, e)
        else:
            return half_division(func, yk, zk, xk, e)

    return xk


if __name__ == "__main__":
    a0, b0, e = int(input("a₀=")), int(input("b₀=")), float(input("e="))
    xk = (a0 + b0)/2

    print(half_division(f, a0, b0, xk, e))
