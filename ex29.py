v = int(input('Qual é a velocidade do veiculo? '))
m = (v - 80) * 7
if v > 80:
    print('Você esta acima do limite de velocidade de 80Km/h!')
    print('Voce deve pagar um multa de R${:.2f}'.format(m))
else:
    print('Você esta dentro do limite permitido')