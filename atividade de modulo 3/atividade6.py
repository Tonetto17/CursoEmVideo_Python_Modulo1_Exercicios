a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f'Menor número é {menor}')
print(f'Maior número é {maior}')