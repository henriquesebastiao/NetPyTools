import sys, os, time

sys.path.insert(0, './modules')

from modules import ip_adress, domain_name

try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(time.strftime('%H:%M:%S', time.localtime()))
    print('NetPyTools v0.1.0')
    print('Author: Henrique Sebastião\n')
    try:
        print('O que deseja fazer hoje?')
        print('1 - Resolver nome de host')
        print('2 - Obter informações sobre um IP')
        print('3 - Obter IP de um domínio')
        print('Pressione Ctrl + C para sair\n')

        option = int(input('>>> '))
        
        # Resolve o nome do host
        if option == 1:
            print(ip_adress.Ip(input('\nEndereço IP: ')).resolve_name())
        # Obtém informações sobre o IP
        elif option == 2:
            ip = input('\nEndereço IP: ')
            print(ip_adress.Ip(ip).get_info('QKntxXoUX9fk5kOhkEdkjgg6dhkETeL7V3ckgshJ'))
        # Obtém o IP de um domínio
        elif option == 3:
            print(domain_name.Domain(input('\nDomínio ou url: ')).get_ip())
    except ValueError:
        print('Opção inválida')
except KeyboardInterrupt:
    print('\nSaindo...')
print()