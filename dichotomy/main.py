def f(x):
    return x**2 + 4*x + 6


def dichotomy(ak, bk, e=1e-5, delta=1e-5):
    assert delta < 2*e, "Delta must be <= 2e"
    l = 2*e
    L2k = abs(bk - ak)
    while L2k > l:
        yk = (ak + bk - delta)/2
        zk = (ak + bk + delta)/2
        if f(yk) <= f(zk):
            bk = zk
        else:
            ak = yk
        L2k = abs(bk - ak)

    return (ak + bk) / 2


if __name__ == "__main__":
    print(dichotomy(-4, 6, 0.5, 0.2))
