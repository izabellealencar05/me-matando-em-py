#uma operadora de telefonia cobra 50.00 reais por um plano basico que da direito a 100 min de telefone, cada min que
#exceder a franquia de 100 min custa 2 reais, fazer um programa para ler a quantidade de min que uma pesdsoa consumiu
#dai mostrar o valor a ser pago

qntd = int(input('digite a quantida de min: '))
if qntd <= 100:
    print('VALOR A PAGAR: 50.00')
elif qntd > 100:
    resto = ((qntd - 100) * 2) + 50
print(f'VALOR A PAGAR: {resto:.2f}')

