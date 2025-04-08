#20)  Elaborar um programa que receba o número de horas trabalhadas e o valor do salário mínimo.
#     Calcule e mostre o salário a receber seguindo as regras abaixo:
#     a) o valor da hora trabalhada vale a metade do salário mínimo;
#     b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora
#     trabalhada;
#     c) o imposto equivale a 3% do salário bruto;
#     d) o salário a receber equivale ao salário bruto menos o imposto

horasTrabalhadas = float(input("Digite o número de horas trabalhadas: "))
salarioMinimo = float(input("Digite o valor do salário mínimo: "))

valorHora = salarioMinimo / 2
salarioBruto = horasTrabalhadas * valorHora
imposto = salarioBruto * 0.03
receber = salarioBruto - imposto

print(f"O salário a receber é: R$ {receber:.2f}")