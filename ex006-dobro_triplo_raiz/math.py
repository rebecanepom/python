#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O dobro de {n} é: {d} \nO triplo de {n} é: {t} \nA raiz quadrada de {n} é: {r:.3f}')

# n = int(input('Digite um número: '))
#print(f'O dobro de {n} é: {n*2} \nO triplo de {n} é: {n*3} \nA raiz quadrada de {n} é: {n**(1/2):.3f}')
