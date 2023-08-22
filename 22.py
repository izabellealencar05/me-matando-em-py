# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo
# pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24
# horas.
inicial = int(input('hora inicial: '))
final = int(input('hora final: '))
duracao = 24 - inicial + final
if inicial < final:
    print(f'o jogo durou {final - inicial} horas')
else:
    print(f'o jogo durou {duracao} horas')
