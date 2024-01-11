#calcular preco com desconto de 10% pra pagamento a vista. e com aumento de 8% pra parcelado.
# qual o preco dele a vista e qual o preco parcelado

preco = float(input('Qual o valor do produto? R$'))
vista = preco - (preco * 10 / 100)
parce = preco + (preco * 8 / 100)
print(f'Se você pagar à vista, terá 10% de desconto e o valor será de R${vista}.\nSe parcelar, terá um aumento de 8% e o valor será de R${parce}.')
print('\nComo gostaria de realizar o pagamento?')