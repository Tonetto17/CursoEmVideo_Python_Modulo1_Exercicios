import math
angulo=float(input('Digite o angulo: '))
seno= math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2}')

cos=math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cos:.2}')

tan=math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {tan:.2}')