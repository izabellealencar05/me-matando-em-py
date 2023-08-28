# Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
# se for o caso.
x = int(input('informe um numero: '))
for i in range (1, x + 1):
    if i % 2 != 0:
        print(i)

