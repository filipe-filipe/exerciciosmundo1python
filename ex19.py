import random
um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
tres = input('Terceiro aluno: ')
quatro = input('Quarto aluno: ')
lista = [um, dois, tres, quatro]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
