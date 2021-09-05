prod = float(input('Digite o preço do produto: '))
desc = prod * 0.05
preco = prod - desc
print('O preço desse produto com desconto de 5% é de R${:.2f}.' .format(preco))