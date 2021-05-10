print('CONVERSOR DE MEDIDAS')
m1 = float(input('Entre com uma medida em metros: '))

dam1 = m1/10**1
hm1 = m1/10**2
km1 = m1/10**3
dm1 = m1*10**1
cm1 = m1*10**2
mm1 = m1*10**3

print('Os valores convertidos de {:.2f}metros são:\nEm decímetros: {:.2f}dm\nEm centímetros: {:.2f}cm\nEm milímetros: {:.2f}mm\nEm decâmetros: {:.2f}dam\nEm hectômetros é: {:.2f}hm\nEm kilômetros é: {:.2f}km'.format(m1,dm1,cm1,mm1,dam1,hm1,km1))