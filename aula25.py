'''
Formatação com f - strings

Caractere de quantidade (><^)

> - esquerda

< - direita

^ - centro

Sinal --> + ou -

Ex.: 0> -100, .1f

Conversation flags - !r !s !a

'''

variavel = 'Bruno'

print(f'{variavel:.^8}')
print(f'{variavel:.<8}')
print(f'{variavel:.>8}')

print(f'{1000.46578367:=+10,.2f}')

print(f'O Exadecimal é {2832:04X}')
