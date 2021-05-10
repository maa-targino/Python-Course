import random

aluno1 = input('Entre com o primeiro nome: ')
aluno2 = input('Entre com o segundo nome: ')
aluno3 = input('Entre com o terceiro nome: ')
aluno4 = input('Entre com o quarto nome: ')

sorteio = random.randint(1, 4)

if sorteio == 1 :
    print(aluno1)
elif sorteio == 2 :
    print(aluno2)
elif sorteio == 3 :
    print(aluno3)
elif sorteio ==4 :
    print(aluno4)