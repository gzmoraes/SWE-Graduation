num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

soma = num1 + num2

if (soma > 30 and num2 > num1):
    print(f"A soma é maior que 30 (o numero maior da some é de {num2})")
elif(soma > 30 and num1 > num2):
    print(f"A soma é maior que 30 (o numero maior da some é de {num1})")
else:
    print (f"A soma não é maior que 30")
