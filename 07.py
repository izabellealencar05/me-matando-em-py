#Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
#quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
#uma mensagem explicativa, conforme exemplo.

nome = str(input('nome: '))
valor = float(input('valor por hora: '))
qntd = float(input('horas trabalhadas: '))
pagamento = valor*qntd
print(f'O pagamento para {nome} deve ser {pagamento}')
