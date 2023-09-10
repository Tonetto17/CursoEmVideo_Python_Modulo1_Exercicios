import random
nome1=input('nome: ')
nome2=input('Nome: ')
nome3=input('Nome: ')
nome4=input('Nome: ')

list=[nome1, nome2, nome3, nome4]
escolhido=random.choice(list)
print(f'O aluno escolhido foi o {escolhido}')