'''
Atividade1:
n1=int(input('Digite um número: '))
n2=int(input('Digite o segundo número: '))
soma=n1+n2
print(f'A soma entre{n1} e {n2} é {soma}')
'''


a=input('Digite algo: ')
print(f'O tipo primitivo é {a}')
print(type(a))
print('Tem espaço?', a.isspace()) 
#MMostra se apenas tem espaço no que foi digitado
print('é um número? ',a.isnumeric())
# Mostra se é um número, ele mostra também se essa string pode ser transformada em um número
print('É alfabetica: ',a.isalpha())
#Se a entrada é alfabetica
print('É alfanumerico? ', a.isalnum())
# Se a entrada é alfanumerico, com entrada de letras é números
print('Esta em letras maiúsculas: ',a.isupper())
# Mostra se toda a entrada está com letras maiúsculas
print('Contém letras minúsculas: ', a.islower())
# Mostra se toda a entrada está com letras minúsculas
print('Está capitalizada? ',a.istitle())
# Mostra se ela tem letras minúsculas e maiúsculas