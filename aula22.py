# Operador lógico 'not'
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha:')

if senha == '123456':
    print('Entando no sistema...')
elif senha != '123456':
    print('Saindo do sistema...')
elif not senha: # inverte o valor da expressão
    print('Você não digitou nada')