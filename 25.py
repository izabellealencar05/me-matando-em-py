# Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
# indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
# e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
# mostrar a mensagem "IMPOSSIVEL CALCULAR"

total = 0
qntd = 0
idade = int(input("Digite a idade (ou um valor negativo para encerrar): "))

if idade < 0: 
    print("IMPOSSÍVEL CALCULAR")
else:
    while idade >= 0:
        total += idade
        qntd += 1
        idade = int(input("Digite a idade de um indivíduo (ou um valor negativo para encerrar): "))

    if qntd > 0: 
        media = total / qntd
        print(f"A idade média dos indivíduos é: {media:.2f}")
    else:
        print("Nenhum dado inserido.")
