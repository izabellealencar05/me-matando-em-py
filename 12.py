#fazer um programa para ler tres coeficientes de uma equacao do segundo grau. usando a formula
# de baskara, calcular e mostrar os valores das raizes x1 e x2 da equacao com quatro casas decimais

coeficiente = float(input('coeficiente de a: '))
coeficiente2 = float(input('coeficiente de b: '))
coeficiente3 = float(input('coeficiente de c: '))
delta = (coeficiente2*coeficiente2) - 4 * coeficiente * coeficiente3
x = (((-1) * coeficiente2)+(delta**0.5))/(2*coeficiente)
x2 = (((-1) * coeficiente2)-(delta**0.5))/(2*coeficiente)
print(f"X1 = {x:.4f}")
print(f'X2 = {x2:.4f}')
