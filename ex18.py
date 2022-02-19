import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o Seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(an, tan))
