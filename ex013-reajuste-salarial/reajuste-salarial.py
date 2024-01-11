#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Nome do funcionário: ')
sal = float(input(f'Qual o salário atual do {nome}? R$'))
nvsal = sal + (sal * 15 / 100)

print(f'O funcionário {nome} recebia R${sal}, com 15% de aumento, passa a receber R${nvsal}')