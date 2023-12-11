#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dólares ela pode comprar.

nome = input('Olá! Qual o seu nome? ')
print(f'Seja Bem Vindo(a) {nome} :)')
real = float(input(f'\n{nome}, quantos reais você tem? R$'))
dolar = real / 5.30
print(f'{nome}, com R${real:.2f} você pode comprar US${dolar:.2f}')
