#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m^2.

larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')