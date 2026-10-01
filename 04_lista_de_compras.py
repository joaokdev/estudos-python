# Exercício 04 - Lista de compras
# Objetivo: praticar listas, repetição e interação com o usuário.

print("=== MINHA LISTA DE COMPRAS ===")

compras = []

while True:
    produto = input("Digite um produto (ou 'fim' para encerrar): ").strip()

    if produto.lower() == "fim":
        break

    if produto:
        compras.append(produto)
        print(f'"{produto}" foi adicionado à lista.')
    else:
        print("Digite um nome válido para o produto.")

print("\n=== RESUMO DA LISTA ===")

if len(compras) == 0:
    print("Sua lista está vazia.")
else:
    for posicao, produto in enumerate(compras, start=1):
        print(f"{posicao}. {produto}")

    print(f"\nTotal de produtos: {len(compras)}")

print("Programa encerrado. Boas compras!")
