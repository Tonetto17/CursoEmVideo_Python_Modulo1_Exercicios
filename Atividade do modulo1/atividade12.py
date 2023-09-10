carro=float(input('Digite o km andado: '))
aluguel=float(input('Dias alugados do carro: '))
dia=aluguel*60
final=carro*0.15
preco=final+dia

print(f'preço a pagar R${preco}')