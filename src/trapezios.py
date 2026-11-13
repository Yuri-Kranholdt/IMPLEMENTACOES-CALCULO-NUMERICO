# MÉTODO DOS TRAPÉZIOS

# Definição da função
def f(x):
    return x**2  # Altere para a função desejada


# Método dos Trapézios
def trapezios(a, b, n):

    h = (b - a) / n

    soma = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        soma = soma + 2 * f(x)

    resultado = (h / 2) * soma

    return resultado


# Programa principal
print("=== MÉTODO DOS TRAPÉZIOS ===")

a = float(input("Digite o limite inferior: "))
b = float(input("Digite o limite superior: "))
n = int(input("Digite o número de subdivisões: "))

if n <= 0:
    print("Erro: o número de subdivisões deve ser positivo.")
else:
    resultado = trapezios(a, b, n)

    print("\nResultado da integral:")
    print("I =", resultado)