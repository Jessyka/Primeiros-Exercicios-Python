def validar_nota(nota1, nota2):
    if nota1 > 5 and nota2 > 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

def main():
    nota1 = int(input('Digite primeira nota:'))
    nota2 = int(input('Digite primeira nota:'))
    validar_nota(nota1, nota2)

main()