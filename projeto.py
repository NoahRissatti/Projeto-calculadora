num1 = float(input('Digite o primeiro número: '))
print('Escolha sua operação: ')
print('Opção 1 - Soma')
print('Opção 2 - Subtração')
print('Opção 3 - Multiplicação')
print('Opção 4 - Dvisão')
opcao = int(input('Digite sua opção: '))
num2 = float(input('Digite o segundo número: '))
if opcao == 1:
    soma = num1 + num2
    print('O resultado é {}'.format(soma))
elif opcao == 2:
    sub = num1 - num2
    print('O resultado é {}'.format(sub))
elif opcao == 3:
    mult = num1 * num2
    print('O resultado é {}'.format(mult))
elif opcao == 4:
    if num2 == 0:
        print('Não há divisão por 0')
    else:
        div = num1 / num2
        print('O resultado é {}'.format(div))