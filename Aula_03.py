# LIST COMPREHENSION COM IF PARA FILTRAR ITENS

#lista = [expressão for item in interable if condição]

meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho','cafeteira', 'microondas', 'iphone']

#FAZENDO FOR TRADICIONAL 

produtos_acima_meta = []
for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)

# FAZENDO COM LIST 

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)