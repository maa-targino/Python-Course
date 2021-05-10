from math import pow, sqrt
print('CALCULA HIPOTENUSA')
c1 = float(input('Entre com o primeiro cateto: '))
c2 = float(input('Entre com o segundo cateto: '))
hip = sqrt(pow(c1,2) + pow(c2,2))
print('O valor da hipotenusa é: {:.2f}'.format(hip))
