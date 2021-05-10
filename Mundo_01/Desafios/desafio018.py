from math import sin, cos, tan, pi
print('CALCULA ANGULO')

""" radA = float(input('Entre com a medida do ângulo em radianos: '))
sinA = sin(radA)
cosA = cos(radA)
tanA = tan(radA)
print("O seu seno é: {:.1f}\nO seu coseno é: {:.1f}\nA sua tangente é: {:.1f}".format(sinA,cosA,tanA)) """

angB = float(input('Entre com a medida do ângulo em graus: '))
sinB = sin(angB*pi/180)
cosB = cos(angB*pi/180)
tanB = tan(angB*pi/180)
print("O seu seno é: {:.1f}\nO seu coseno é: {:.1f}\nA sua tangente é: {:.1f}".format(sinB,cosB,tanB))