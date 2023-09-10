num1=float(input('Valor 1: '))
num2=float(input('Valor 2: '))
num3=float(input('Valor 3: '))
if num1<num2+num3 and num2<num1+num3 and num3< num1+num2:
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')