# Exercício 01 - Calculadora simples
# Objetivo: praticar entrada de dados, conversão de tipos e operações matemáticas.

print("=== CALCULADORA SIMPLES ===")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção desejada: ")

if opcao == "1":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif opcao == "2":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif opcao == "3":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif opcao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    else:
        print("Não é possível dividir um número por zero.")
else:
    print("Opção inválida. Execute o programa novamente.")
