def integration(f, a, b, N = 50):
    y_right = f[1:]
    y_left = f[:-1]
    dx = (b - a)/N
    T = (dx/2)* (sum(y_right) + sum(y_left))

    return T