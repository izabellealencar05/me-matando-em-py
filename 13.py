#fazer um programa para ler tres numeros inteiros. em seguida mostrar qual o menor dentre os tres numeros lidos, em caso de empate ,mostrar apenas uma vez
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
if a < b and a < c:
    print(f"MENOR: {a}")
elif b < a and b < c:
    print(f'MENOR: {b}')
else:
    print(f"MENOR: {c}")
