k = 0.38196601125010515179541316563435  # 3 - √5 / 2


def f(x):
    return x**2 + 4*x + 6


def golden(a, b, e=1e-7):
    y = k * (b - a) + a
    z = a + b - y
    fy = f(y); fz = f(z)
    while abs(b-a) > e:
        if fy <= fz:
            b = z
            z = y
            y = a + b - y
            fz = fy
            fy = f(y)
        else:
            a = y
            y = z
            z = a + b - z
            fy = fz
            fz = f(z)

    return (a + b)/2


def main():
    print(golden(-4, 6, 0.5))


if __name__ == '__main__':
    main()
