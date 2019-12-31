# Primeiros-Exercicios-Python

**Exercicios realizados durante curso "Introducao a linguagem python".**
**Python 3:**

*Operacoes Matemáticas:*
+ [+] soma
+ [-] subtracao
+ [ * ] multiplicacao
+ [ ** ] exponencial
+ [/] divisao
+ [%] Modulo

+ [=] operador de atribuicao 

*Operadores relacionais:*

+ [==] igual
+ [!=] diferente
+ [>] maior que
+ [<] menor que
+ [>=] maior ou igual que
+ [<=] menor ou igual que

*Operadores Lógicos:*
+ and -> e
+ or -> ou

*Estruturas condicionais:*
``` python
if condicao:
    comando a executar.
else:
    comando a executar.
```
*Estrutura de repeticao:*
``` python
while condicao:
    comando a executar.

for item in lista:
    comando
```

*Leitura de arquivos:*
``` python
variavel = open(name, modo)
#Lendo o arquivo:
read() #Le o arquivo inteiro.
readLine() #Le uma linha.
readLines() #Le o aquivo e armazena em uma lista.
```
Modos:
+ [r] somente leitura
+ [w] escrita (caso arquivo ja exista, ele sera sobrescrito)
+ [a] leitura e escrita (adicionar novo conteuni ao fim do arquivo)
+ [r+] leitura e escrita
+ [w+] escrita
+ [a+] leitura e escrita

*Arrays:*
+ [len(lista)] tamanho da lista
+ [_.append(item)] adicionar novo item ao final da lista
+ [del lista[indice] ] remover elemento da lista
+ [del lista[:] ] limpar a lista