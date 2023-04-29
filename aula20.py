# Operadores lógicos
# And (e) or (ou) not (não)

# Quando uma condição tem dois valores, ambos tem que ser true, pois 
# se uma das duas condições for false a espressão toda será pulada.

# Valores que são considerados false: 0; 0.0; false ('' = string vazia )

print('----Sistema 2.0----')
senha = input('Qual a senha ?')
entrada = input('[E]ntrar [S]air: ')



senha_correta = '123456'

if entrada == 'S':
    print('Saindo do sistema...')
elif entrada == 'E' and senha == senha_correta:
    print('Entrando no sistema...')
elif senha != senha_correta:
    print('Senha incorreta tente novamente !')


# Avaliação de curto circuito
print(True and False and True)



    

