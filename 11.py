#ler duas notas que o aluno obteve no primiero e segndo semestre de uma disciplina anual, em seguida
# mostrar a nota final que o aluno obteve no ano, caso a nota final do aluno seja inferior a 60.0 mostrar a mensagem reprovado

nota = float(input('qual a nota do primeiro semestre? '))
nota2 = float(input('qual a nota do segundo semestre? '))
nota_final = (nota + nota2)
print(f'NOTA FINAL: {nota_final:.2f}')
if nota_final >= 60.0:
    print("APROVADO")
else:
    print("REPROVADO")
