# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
# mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
# programa deve finalizar quando forem digitados dois valores iguais.
while True:
    x = float(input('informe um numero: '))
    y = int(input('informe outro numero: '))
    if x > y:
        print('DECRESCENTE')
    elif x < y:
        print("CRESCENTE")
    else:
        break

