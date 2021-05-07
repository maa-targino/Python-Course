print('CALCULADORA DE ALUGUEL DE CARRO')
quatidadeDias = int(input('Por quantos dias o automóvel foi alugado? '))
valorDiaria = float(input('Qual é o valor da diária da locação do automóvel? '))
quilometragem = float(input('Qual foi a distância percorrida em quilômetros pelo automóvel? '))
valorFinal = quatidadeDias*valorDiaria + quilometragem*0.5
print('O valor final da locação do automóvel foi de: R${:.2f}'.format(valorFinal))