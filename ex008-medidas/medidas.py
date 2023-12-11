#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Digite uma distância em metros: '))

print(f'A medida de {m}m corresponde a {m*10:.0f}dm ')
print(f'A medida de {m}m corresponde a {m*100:.0f}cm ')
print(f'A medida de {m}m corresponde a {m*1000:.0f}mm ')
print(f'A medida de {m}m corresponde a {m/10:.0f}dam ')
print(f'A medida de {m}m corresponde a {m/100:.0f}hm ')
print(f'A medida de {m}m corresponde a {m/1000:.0f}km ')

# Conversão de Metros para:
# dm(decímetro) = valor*10
# cm(centímetro) = valor*100
# mm(milímetro) = valor*1000
# dam(decâmetro) = valor/10
# hm(hectômetro) = valor/100
# km(quilômetro) = valor/1000