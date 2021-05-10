print('CALCULADORA DE TINTA')
h = float(input('Entre com a altura da parede: '))
l = float(input('Entre com a largura da parede: '))
a = h*l
v = a/2 
print('O volume de tinta necessário para pintar {:.2f}m² de parede é: {:.2f}L'.format(a,v))
