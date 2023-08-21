#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
#ostrar o valor do troco a ser devolvido ao cliente. 

preco = float(input("qual o preco do produto? "))
qntd = int(input("qual a quantidade? "))
dinheiro = float(input("dinheiro recebido: "))
quanto = preco * qntd
troco = dinheiro - quanto
print(f"TROCO: {troco:.2f}")
