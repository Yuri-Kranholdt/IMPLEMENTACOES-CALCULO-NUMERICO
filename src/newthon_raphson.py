def newton_raphson(f, df, x0, tol=1e-3, max_iter=100):
    x = x0

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivada igual a zero.")
            return None

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    print("O método não convergiu.")
    return x


def f(x):
    # função
    return x**3 - 2*x - 5


def df(x):
    # derivada da função
    return 3*x**2 - 2


print(newton_raphson(f, df, 2))