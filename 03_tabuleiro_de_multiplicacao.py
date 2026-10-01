# Exercício 03 - Tabuada
# Objetivo: praticar laços de repetição com for e a função range().

print("=== GERADOR DE TABUADA ===")

numero = int(input("Qual número você quer consultar? "))

print(f"\nTabuada do {numero}:")

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

print("\nTabuada finalizada!")
