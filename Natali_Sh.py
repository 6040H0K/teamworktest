def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_result():
        nonlocal a
        nonlocal b
        nonlocal c
        discreminant = pow(b, 2) - 4 * a * c
        if discreminant >= 0:
            x1 = (-b - (discreminant ** 0.5)) / 2 * a
            x2 = (-b + (discreminant ** 0.5)) / 2 * a
            return x1, x2
