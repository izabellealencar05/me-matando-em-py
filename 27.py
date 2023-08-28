# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.
num = int(input('escolha um numero para a tabuada: '))
print('---------------------')
print(f' TABUDADA DO {num}  ')
print('---------------------')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
print('---------------------')
print('         FIM         ')
print('---------------------')
