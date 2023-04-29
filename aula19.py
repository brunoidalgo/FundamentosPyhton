print('----- Bem vindo ao exercício de Python sobre comparação -----')

primeiro_valor = int(input('Qual o primeiro valor :'));
segundo_valor = int(input('Qual o segundo valor :'));



if primeiro_valor > segundo_valor:
    print(f'Primeiro valor: {primeiro_valor} é maior do que o segundo valor: {segundo_valor}');
elif segundo_valor > primeiro_valor:
    print(f'Primeiro valor: {primeiro_valor} é menor do que o segundo valor: {segundo_valor}');
elif primeiro_valor == segundo_valor:
    print('Ambos os valores são iguais');
else:
    print('Opção Inválida')