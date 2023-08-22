# O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
# e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
# ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
# valor restante conforme exemplo.

preco = float(input('PRECO UNITARIO DO PRODUTO: '))
qntd = int(input('QUANTIDADE DE PRODUTO: '))
recebido = float(input('VALOR RECEBIDO: '))
valor = preco * qntd
troco = recebido - valor
print(f"TROCO: {troco:.2f}")

