#1) Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o
#   trabalhador pode ou não se aposentar. As condições para aposentadoria são:
#    • Ter pelo menos 65 anos,
#    • Ou ter trabalhado pelo menos 30 anos,
#    • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade?: "))
tempoServico = int(input("Qual seu tempo de serviço?: "))

if(idade >= 65 or tempoServico >= 30):
    print("Você ja pode se aposentar!")
elif (idade >= 60 and tempoServico >= 25):
    print("Você ja pode se aposentar!")
else:
  print ("Você não pode se aposentar!")