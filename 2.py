#Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
#da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos. 

base = float(input("digite o valor da base: "))
altura = float(input("digite o valor da altura: "))
area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = (base**2 + altura**2)**0.5
print(f"o valor da area é {area:.2f}")
print(f"perimetro é {perimetro:.2f}")
print(f"diagonal é {diagonal:.2f}")
