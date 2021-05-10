print('CALCULADORA DE MEDIA')
n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
m = (n1+n2)/2
print('A média de {} e {} é: {:.2f}'.format(n1,n2,m))
if m>=7 :
    print('Parabéns! Você foi aprovado!')
elif m<7:
    print('Infelizmente você não foi aprovado. Estude mais da próxima vez!')