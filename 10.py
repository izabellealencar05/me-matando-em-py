#Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
#formato horas:minutos:segundos. 
duracao = float(input("quantos segs? "))
hora = duracao/3600
min = (duracao%3600)/60
segs = duracao%60
print(f'{hora:.0f}:{min:.0f}:{segs:.0f}')
