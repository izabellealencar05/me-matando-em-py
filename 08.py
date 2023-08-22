#Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
#combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
#médio do carro, com três casas decimais.

distancia = float(input('DISTANCIA PERCORRIDA: '))
combustivel = float(input('COMBUSTIVEL GASTO: '))
consumo_medio = distancia/combustivel
print(f'o consumo medio foi {consumo_medio:.3f}')
