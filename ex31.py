v = int(input('Qual a distancia em Km da sua viagem? '))
if v >= 200:
    print('O custo da sua viagem sera de R$ {:.2f}'.format(v * 0.50))
else:
    print('O custo da sua viagem sera de R$ {:.2f}'.format(v * 0.45))
    

    