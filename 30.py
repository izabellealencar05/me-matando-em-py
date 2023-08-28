# Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
# segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.
while True:
    num = float(input('digite um numero: '))
    num2 = float(input('digite outro numero: '))

    if num2 == 0:

        print("IMPOSSIVEL DE CALCULAR!")
        continue
    else:
        divisao = num/num2
        print(f'o resultado da divisao é {divisao:.2f}')
        break
