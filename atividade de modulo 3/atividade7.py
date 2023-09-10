salario=float(input('Digite um valor: '))
if salario>=1250:
    a=(10/100)*salario
    final=salario+a
    print(f'Aumento de R${final}')
else:
    b=(15/100)*salario
    total=salario+b
    print(f'Aumento de R${total}')