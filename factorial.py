# -*- coding: utf-8 -*-

def factorial(number):
    if number == 0:
        return 1
    
    return number * factorial(number-1)

def main():
    num = int(input("Digite um número inteiro:"))
    print("Factorial %d = %d" % (num, factorial(num)))


main()
