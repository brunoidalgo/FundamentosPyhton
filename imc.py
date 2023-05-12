# Calculadora de Imc em Python

print('-----Calculo de Imc-----')
print(), print()
entrada = str(input("Quer ligar o sistema ?"))

if (entrada == "Sim" or "sim" or "s" and "S"):
    print("Sistema iniciado!")
    nome = input("Qual o seu nome ?")
    peso = float(input("Qual seu peso em Kg ?"))
    altura = float(input("Qual sua altura em Metros ?"))
    idade = int(input("Qual sua idade ?"))

    imc = peso // (altura * altura)

    print(
        f"Seu nome é {nome} seu imc é {imc} você pesa {peso} e tem a altura de {altura} ")
else:
    print("Ok, saindo do sistema")
