print('NetPyTools v0.1.0')
print('Author: Henrique Sebastião')

while True:
    try:
        print('O que deseja fazer hoje?')
        print('1 - Verificar se um site está online')
        print('2 - Obter informações sobre um site')
        print('3 - Obter informações sobre um IP')
        print('4 - Obter informações sobre um domínio')
        print('0 - Sair')

        option = int(input('Opção: '))
    except ValueError:
        print('Opção inválida')
        continue