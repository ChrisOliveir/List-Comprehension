# ESTRUTURA 

# lista = [expressão for item in iterable]

preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeteria', 'microondas', 'iphone']

'''
Digamos que o imposto sobre os produtos é de 30% ou seja 0.3. Como eu faria para criar uma lista com os valores de imposto de cada item?

'''
imposto = []
for i in preco_produtos:
    imposto.append(i * 0.3)
print(imposto)
    
# USANDO A LIST

impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)