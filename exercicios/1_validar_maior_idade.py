def validar_idade(idade):
    if idade >= 18:
        print('Maior de idade.')
    else:
        print('Menor de idade.')

def main():
    idade = int(input('Digite sua idade:'))
    validar_idade(idade)

main()