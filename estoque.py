estoque = {
    "camisa" : 50,
    "calça" : 15,
    "boné": 25,
    "tenis nike" : 35,
}
#Mostrar estoque atual
print("estoque atual: ")
for produto , quantidade in estoque.items():
    print(f"{produto} : {quantidade}")

#Pedindo dados para o usuario do sistema
nome_produto = input("\ninforme o nome do produto vendido: ")
quantidade_vendida = int (input("\ninforme a quantidade vendida:"))
#Atualizar o estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print ("venda realizada com sucesso !!")
        
else:
    print("produto nao encontrado")

#Mostrar estoque atualizado
for produto, quantidade in estoque .items():
    print (f"{produto} , {quantidade}")
