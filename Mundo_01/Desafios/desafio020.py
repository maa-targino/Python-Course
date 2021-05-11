from random import shuffle

aluno1 = input('Entre com o primeiro nome: ')
aluno2 = input('Entre com o segundo nome: ')
aluno3 = input('Entre com o terceiro nome: ')
aluno4 = input('Entre com o quarto nome: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('Os trabalhos vão ser apresentados respectivamente pelos alunos: {}'.format(lista))