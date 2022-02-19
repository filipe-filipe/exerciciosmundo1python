s = int(input('Qual é o seu salario? '))
if s >= 1250:
    print('Seu salario tera um aumento de 10% e ficara R${:.2f}'.format(s * 10 / 100 + s))
else:
    print('Seu salario tera um aumento de 15% e ficara R${:.2f}'.format(s * 15 / 100 +s))