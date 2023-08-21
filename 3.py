#Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
#nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. 

nome = str(input("qual o seu nome? "))
nome2 = str(input("qual o seu nome? "))
idade = int(input("qual a sua idade? "))
idade2 = int(input("qual a sua idade? "))
media = (idade + idade2)/2
print(f"a idade media de {nome} e {nome2} é {media:.1f} anos")



