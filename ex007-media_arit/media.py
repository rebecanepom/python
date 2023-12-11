#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('             Escola dos Burros Inteligentes')
nome = input('\nQual o nome do aluno? ')
n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
n3 = float(input('\nDigite a terceira nota: '))
media = (n1 + n2 + n3)/2

if media < 7.0:
    print(f'A média é {media} e infelizmente o aluno {nome} está reprovado :(')
else:
    print(f'A média é {media} e o aluno {nome} está aprovado :)')