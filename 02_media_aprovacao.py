# Exercício 02 - Média e situação do aluno
# Objetivo: trabalhar com variáveis, cálculos e estruturas condicionais.

print("=== SISTEMA DE MÉDIA ===")

nome = input("Nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nAluno: {nome}")
print(f"Média final: {media:.2f}")

if media >= 7:
    print("Situação: Aprovado(a)")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado(a)")
