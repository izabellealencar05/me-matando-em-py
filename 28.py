# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
# impares entre eles.
x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

if x > y:
    x, y = y, x
soma = 0

for num in range(x + 1, y):
    if num % 2 != 0:
        soma += num
print(f"A soma dos impares é: {soma}")
