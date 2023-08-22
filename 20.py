# Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
# números podem ser digitados em qualquer ordem.
x = int(input('digite um inteiro: '))
y = int(input('digite outro inteiro: '))
if x % y == 0 or y % x == 0:
    print('sao múltiplos')
else:
    print('nao sao multiplos')
