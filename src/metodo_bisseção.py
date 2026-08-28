import pandas as pd


def bissection(interval, function, stop_cond=None, n_iteractions=0, debug=False):

    if stop_cond and n_iteractions: raise ValueError("Só é possivel escolher um dos métodos")

    a = interval[0]
    b = interval[1]

    if function(a) * function(b) >= 0:
        raise ValueError("Intervalo com número de mesmo sinal")

    c = 0
    debug_rows = []

    if n_iteractions:
        for i in range(n_iteractions):
            c = (a + b) / 2
            fc = function(c)
            fa = function(a)
            fb = function(b)

            if debug:
                debug_rows.append({
                    "K": i,
                    "A": a,
                    "B": b,
                    "C": c,
                    "F(A)": fa,
                    "F(B)": fb,
                    "F(C)": fc,
                })

            if fc * fa >= 0:
                a = c

            elif fc * fb >= 0:
                b = c

    elif stop_cond:
        counter = 0
        while True:
            c = (a + b) / 2
            fc = function(c)
            fc = function(c)
            fa = function(a)
            fb = function(b)

            if debug:
                debug_rows.append({
                    "K": counter,
                    "A": a,
                    "B": b,
                    "C": c,
                    "F(A)": fa,
                    "F(B)": fb,
                    "F(C)": fc,
                })

            if abs(stop_cond(fc)): break

            if fc * fa >= 0:
                a = c

            elif fc * fb >= 0:
                b = c
            counter += 1
    else:
        raise ValueError("Opção inválida")

    if debug:
        df_debug = pd.DataFrame(debug_rows)
        print(df_debug.to_string(index=False))

    return c


def function_n_linear(x):
    #return (x**2) - (9*x) + 8
    return (x**2) - 3
    #return x**2 - 2


def stop_condition(fc):
    return abs(fc) <= 0.01


print(bissection([1, 2], function_n_linear, stop_condition, debug=True))