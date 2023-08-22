# Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
# isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
# informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
# duas casas decimais.
escala = str(input('qual escala voce vai digitar? (c/f) '))
if escala == 'C' or escala == 'c':
    celsius = float(input('digite a temperatura em celsius: '))
    valor = (celsius * 1.8) + 32
    print(f'Temperatura equivalente em Fahrenheit: {valor:.2f}')
elif escala == 'F' or escala == 'f':
    fahrenheit = float(input('digite a temperatura em fahreinheit: '))
    valor2 = (fahrenheit - 32)/1.8
    print(f'Temperatura equivalente em celsius: {valor2:.2f}')
