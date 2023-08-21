#Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
#com quatro casas decimais):
#a) a área do quadrado que tem lado A
#b) a área do triângulo retângulo que base A e altura B
#c) a área do trapézio que tem bases A e B, e altura C 

a = float(input('digite a medidade de A: '))
b = float(input('digite a medidade de B: '))
c = float(input('digite a medidade de C: '))
quadrado = a*a
triangulo = (a * b)/2
trapezio = ((a + b) * c)/2
print(f'AREA DO QUADRADO: {quadrado:.4f}')
print(f'AREA DO TRIANGULO RETANGULO: {triangulo:.4f}')
print(f'AREA DI TRAPEZIO: {trapezio:.4f}')
