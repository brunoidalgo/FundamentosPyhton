# Operador lógico Or (Ou)
# Não irá parar na condição false

# Se qualquer condição for verdadeira, a expressaõ será executada

# Avaliação de curto circuito
print(True or False )


print('----Sistema 2.0----')

entrada = input('[E]ntrar [S]air: ')
senha = input('Qual a senha ?') or 'Sem senha'



senha_correta = '123456'

if entrada == 'S':
    print('Saindo do sistema...')
elif (entrada == 'E' or entrada == 'e') and senha == senha_correta:
    print('Entrando no sistema...')
elif senha != senha_correta:
    print('Senha incorreta tente novamente !')