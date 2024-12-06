
produtos_disponiveis = {
    "arroz": 5.00,
    "feijao": 7.50,
    "macarrao": 3.00,
    "oleo": 8.00,
    "leite": 4.50
}

carrinho = []

print("Bem-vindo ao Mercado!")
print("Produtos disponíveis:")
for produto, preco in produtos_disponiveis.items():
    print(f"{produto.capitalize()}: R$ {preco:.2f}")

while True:
    produto_escolhido = input("\nDigite o nome do produto que deseja adicionar ao carrinho (ou 'sair' para finalizar): ").lower()
    
    if produto_escolhido == "sair":
        break
    
    if produto_escolhido in produtos_disponiveis:
        quantidade = int(input(f"Quantas unidades de {produto_escolhido} você deseja adicionar? "))
        carrinho.append((produto_escolhido, quantidade))
    else:
        print("Produto não disponível. Tente novamente.")

valor_total = 0
for produto, quantidade in carrinho:
    valor_total += produtos_disponiveis[produto] * quantidade

desconto = 0
if valor_total > 70:  
    desconto = valor_total * 0.10
    valor_total -= desconto

print("\nResumo da compra:")
for produto, quantidade in carrinho:
    print(f"{produto.capitalize()} (x{quantidade}): R$ {produtos_disponiveis[produto] * quantidade:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")

forma_pagamento = input("\nEscolha a forma de pagamento (dinheiro/cartão): ").lower()
if forma_pagamento == "dinheiro":
    print("Pagamento realizado em dinheiro. Obrigado pela compra!")
elif forma_pagamento == "cartão":
    print("Pagamento realizado no cartão. Obrigado pela compra!")
else:
    print("Forma de pagamento inválida.")
