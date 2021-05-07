print('CALCULADORA DE DOLAR')
brl = float(input('Entre com o valor em BRL que você possui: '))
usd = brl//5.21
troco = brl%5.21
print('\nVocê possui RS{:.2f}'.format(brl))
if brl < 5.21 :
    print('Você não possui dinheiro o suficiente para comprar USD.')
else :
    print('Com essa quantia você pode comprar no máximo U${:.2f} e sobram R${:.2f} de troco.'.format(usd,troco))
