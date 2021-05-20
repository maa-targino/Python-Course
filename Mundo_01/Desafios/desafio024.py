print('ENCONTRA SANTO\n')
cidade = input('Entre com o nome da sua cidade: ')
santo = cidade.count('Santo',0,5)
santa = cidade.count('Santa',0,5)
sao = cidade.count('São',0,3)
if santo == 1 or santa == 1 or sao == 1:
    print('Sua cidade é santa!!!')
elif santo == 0 and santa == 0 and sao == 0:
    print('Sinto muito, sua cidade não é santa.')