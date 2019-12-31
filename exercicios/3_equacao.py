from math import sqrt

def delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def primeira_raiz(a, b, c):
    dividendo = (-b) + sqrt(delta(a, b, c))
    divisor = 2 * a
    return dividendo / divisor


def segunda_raiz(a, b, c):
    dividendo = (-b) - sqrt(delta(a, b, c))
    divisor = 2 * a
    return dividendo / divisor

def main():
    a = int(input('Digite o valor de a:'))
    b = int(input('Digite o valor de b:'))
    c = int(input('Digite o valor de c:'))

    print('primeira raiz: %0.2f' %(primeira_raiz(a, b, c)))
    print('segunda raiz: %0.2f' %(segunda_raiz(a, b, c)))

main()