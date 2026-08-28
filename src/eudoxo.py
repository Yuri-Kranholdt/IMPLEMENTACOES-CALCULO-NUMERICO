def sqrt(value, n_iter):
    x = (1 + value) / 2
    for i in range(1, n_iter):
        x = ((value / x) + x) / 2
    return x


print(sqrt(3, 10))