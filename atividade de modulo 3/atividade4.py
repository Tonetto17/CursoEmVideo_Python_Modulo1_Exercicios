distancia=float(input('Digite o a distância da viagem: '))
if distancia<= 200:
    a=distancia*0.50
    print(f'O valor da viagem foi R${a}')
else:
    b=distancia*0.45
    print(f'O valor da viagem foi de R${b}')