velocidade=float(input('Digite a velocidade do carro: '))
if velocidade>=80:
    print('MULTADO')
    multa=(velocidade-80)*7
    print(f'Você teve uma multa de R${multa}')
else:
    print('Você não foi multado')