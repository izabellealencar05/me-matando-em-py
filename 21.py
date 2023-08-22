# Uma empresa vai conceder um aumento percentual de salário aos seus funcionários dependendo de quanto
# cada pessoa ganha, conforme tabela ao lado. Fazer um programa para ler o salário de uma pessoa, daí mostrar
# qual o novo salário desta pessoa depois do aumento, quanto foi o aumento e qual foi a porcentagem de aumento.

salario = float(input('Qual o salário? '))
if salario <= 1000:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    porcentagem_aumento = 20
elif salario <= 3000:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    porcentagem_aumento = 15
elif salario <= 8000:
    aumento = salario * 0.1
    novo_salario = salario + aumento
    porcentagem_aumento = 10
else:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    porcentagem_aumento = 5

print('NOVO SALARIO:', novo_salario)
print('AUMENTO:', aumento)
print('PORCENTAGEM:', porcentagem_aumento, '%')
