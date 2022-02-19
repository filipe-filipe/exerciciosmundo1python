l1 = float(input('Digite uma medida do lado: '))
l2 = float(input('Digite outra medida de lado: '))
l3 = float(input('Digite outra medida de lado: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print('Essas medidas podem formar um triangulo')
else:
    print('Essas medidas não podem formar um triangulo')
