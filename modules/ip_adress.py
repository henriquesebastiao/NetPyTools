import socket, ipbase

class Ip:
    def __init__(self, ip):
        self.ip = ip
    
    def resolve_name(self):
        """Retorna o nome do host do IP informado."""
        try:
            nome_host = socket.gethostbyaddr(self.ip)[0]
            return nome_host
        except socket.herror:
            return "Unable to resolve hostname"

    def get_info(self, api_key, caminho='results/result.txt'):
        """Imprime informações sobre o IP informado."""
        
        # Informa o status de uso da API
        client = ipbase.Client(api_key)
        print('Status da API: ')
        status = client.status()
        print(f"{status['quotas']['month']['remaining']} consultas restantes no mês.\n")
        
        # Retorna as informações do IP
        request = client.info(self.ip)
        
        result = f"""Endereço IP: {request['data']['ip']}
Hostname: {request['data']['hostname']}
Tipo: {request['data']['range_type']['description']}
Organização: {request['data']['connection']['organization']}
ISP: {request['data']['connection']['isp']}
Range: {request['data']['connection']['range']}
              
Localização:
Latitude: {request['data']['location']['latitude']}
Longitude: {request['data']['location']['longitude']}
Cidade: {request['data']['location']['city']['name']}
CEP: {request['data']['location']['zip']}
Estado: {request['data']['location']['region']['name']}
Continente: {request['data']['location']['continent']['name']}
País: {request['data']['location']['country']['alpha2']}, {request['data']['location']['country']['alpha3']}, {request['data']['location']['country']['name']}
Código Telefone: {request['data']['location']['country']['calling_codes'][0]}
                            
Hora atual: {request['data']['timezone']['current_time']}
Timezone: {request['data']['timezone']['id']}
Código: {request['data']['timezone']['code']}"""
        
        # Salva o resultado em um arquivo
        with open(caminho, 'w', encoding="utf-8") as file:
            file.write(result)
        
        return result