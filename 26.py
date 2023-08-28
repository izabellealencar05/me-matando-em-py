# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
# senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
# for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
# encerrado. Considere que a senha correta é o valor 2002
correto = 2002

while True:
    senha = int(input('digite a senha: '))
    if senha != correto:
        print('senha invalida! continue tentando')
        continue
    else:
        print('voce acertou a senha')
    break
