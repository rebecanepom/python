#import emoji
#print(emoji.emojize('Olá, Mundo :globe_showing_Americas:', language='alias'))

#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

'''from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')'''

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')