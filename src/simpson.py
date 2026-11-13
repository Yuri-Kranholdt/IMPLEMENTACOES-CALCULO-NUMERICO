# Implementação do método númerico Regra Composta de Simpson
import math

def simpson(func, n, a, b):
  if (n % 2 != 0):
    n += 1

  h = (b - a) / n
  
  change = False
  res = func(a) + func(b)
  
  for i in range(1, n):
    x = a + i*h
    coeficiente = 4 if not change else 2 
    res += coeficiente * func(x)
    change = not change
    
  return res * (h/3)

# ----- TESTES -------
def sen(theta):
  return math.sin(theta)

#print(simpson(sen, 4, 0, math.pi))

def ex(x):
  return math.exp(x)

#print(simpson(ex, 4, 0, 2))

def erf_integral(t):
    return math.exp(-t ** 2)

def erf(x):
    return (2/math.sqrt(math.pi)) * simpson(erf_integral, 20, 0, x) 

def gaussian(x, media, desvio_padrao):
    z = (x - media) / desvio_padrao
    return 1/2 * (1 + erf(z/math.sqrt(2))) # P(X <= x)

print(gaussian(540, 500, 20))