def calculadora(valor1, valor2, sinal):
    if sinal == '+':
        print('Soma: %d' %(valor1 + valor2)) 
    elif sinal == '-':
        print('Subtracao: %d' %(valor1 - valor2)) 
    elif sinal == '*':
        print('Multiplicacao: %d' %(valor1 * valor2))
    elif sinal == '/':
        print('Divisao: %d' %(valor1 / valor2))
    else:
        print('Operacao invalida')

def main():
    valor1 = int(input('Digite o primeiro valor:'))
    valor2 = int(input('Digite o segundo valor:'))
    sinal = input('Digite o sinal:')
    calculadora(valor1, valor2, sinal)

main()