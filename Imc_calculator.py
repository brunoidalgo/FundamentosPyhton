# if, elif e else
# se, se não se, se não



# entrada = input('Quer ligar o sistema ?')

# if entrada == 'sim':
#     print('Ligando sistema...')
# elif entrada == 'nao':
#     print('Desligando sistema...')
# else :
#     print('Não entendi, digite sim ou não.')

entrada = input('Quer ligar o sistema ?')

if entrada == 'sim':
    print('Medindo seu IMC...')
    nome = input('Qual seu nome ?')
    peso = int(input('Qual seu peso ?'))
    altura = float(input('Qual sua altura ?'))
    imc = peso // (altura * altura)
    linha = f'{nome} tem a altura de: {altura:.2f}m e pesa: {peso:.2f}kg e tem o imc de: {imc}'
    print(linha)
elif entrada == 'nao':
    print('Desligando sistema...')
else :
    print('Não entendi, digite sim ou não.')


