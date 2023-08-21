#Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
#casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
#o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
#duas casas decimais, conforme exemplo. 

largura = float(input('digite a largura do terreno: '))
comprimento = float(input("digite o comprimento do terreno: "))
valor = float(input("qual o valor do metro quadrado? "))
area = comprimento * largura
preco = area * valor
print(f'A área do terreno é: {area:.2f}')
print(f"o preco do terreno é: {preco:.2f}")


