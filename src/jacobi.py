import math


def norm(matrix):
    # calcula tamanho do vetor, usa de metrica para saber se o método está convergindo
    return math.sqrt(sum(value ** 2 for value in matrix))


def jacobi(A, b):
    X = [0.0] * len(b)  # xK, yK, zK... com chute inicial igual a zero
    x = [0.0] * len(b)  # temp

    E = 0.00001  # precisão
    m = 1000  # numero maximo de iterações
    ni = 0  # contador de iterações

    while ni < m:
        for i in range(len(b)):
            soma = 0.0
            conv = 0.0

            for j in range(len(b)):
                if j != i:
                    conv += abs(A[i][j])
                    soma += A[i][j] * X[j] / A[i][i]

            if A[i][i] <= conv:
                raise ValueError("Condição de Convergência não atendida")

            x[i] = (b[i] / A[i][i]) - soma

        if abs(norm(x) - norm(X)) < E:  # compara quanto mudou da iteração anterior
            break
        else:
            X = x.copy()

        ni += 1

    return X

#a = [
    #[1, 1, -2],
    #[3, 1, -1],
    #[2, 1, 1]
#]

#b = [-3, 2, 7]

a = [
    [5, 1, -1],
    [1, 6, -1],
    [2, -1, 6]
]

b = [5, 8, 4]

print(jacobi(a, b))