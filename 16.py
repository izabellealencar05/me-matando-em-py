# Fazer um programa para ler a quantidade de glicose
# no sangue de uma pessoa e depois mostrar na tela a
# classificação desta glicose de acordo com a tabela de
# referência ao lado
qntd = float(input("qual a quantidade de glicose? "))
if qntd <= 100:
    print('NORMAL')
elif qntd > 100 and qntd <= 140:
    print("ELEVADO")
else:
    print('DIABETES')
