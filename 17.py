# No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior
# distância que conseguir.Você deve criar um programa para, dadas as medidas das
# três tentativas de lançamento, informar qual foi a maior
tentativa = float(input("qual foi a distancia? "))
tentativa2 = float(input("qual foi a distancia? "))
tentativa3 = float(input("qual foi a distancia? "))
maior = max(tentativa, tentativa2, tentativa3)
print(f"A MAIOR DISTANCIA FOI: {maior}")
