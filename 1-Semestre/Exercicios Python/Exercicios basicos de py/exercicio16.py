#16) Elaborar um programa que leia 3 notas de um aluno e calcule a média final deste aluno.
#    Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

peso1 = 2
peso2 = 3
peso3 = 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"A média final do aluno é: {media:.2f}")
