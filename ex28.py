import random
n = random.randint(0, 5)
r = int(input('Advinhe um numero entre 0 e 5 que o computador pensou: '))
if r == n:
    print('Você acertou! a resposta é {}!'.format(n))
else:
    print('Você errou, a resposta era {} :('.format(n))
