# Uma lanchonete possui vários produtos. Cada produto possui um código
# e um preço. Você deve fazer um programa para ler o código e a
# quantidade comprada de um produto (suponha um código válido), e daí
# informar qual o valor a ser pago, com duas casas decimais, conforme
# tabela de produtos ao lado.
codigo = int(input('digite o codigo do produto: '))
qntd = int(input('qual a quantidade? '))
if codigo == 1:
    print('valor a pagar: ', 5 * qntd)
elif codigo == 2:
    print('valor a pagar: ', 3.5 * qntd)
elif codigo == 3:
    print('valor a pagar: ', 4.8 * qntd)
elif codigo == 4:
    print('valor a pagar: ', 8.9 * qntd)
elif codigo == 5:
    print('valor a pagar: ', 7.32 * qntd)
