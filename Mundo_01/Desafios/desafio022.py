name = input('Entre com o seu nome: ')
print('Minúsculas: {}'.format(name.lower()))
print('Maiúsculas: {}'.format(name.upper()))
print('Número de caracteres: {}'.format((len(name))-(name.count(' '))))
firstname = name.split()[0]
print('Primeiro nome: {}'.format(firstname))