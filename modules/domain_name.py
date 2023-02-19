import socket

class Domain:
    def __init__(self, domain):
        self.domain = domain

    def get_ip(self):
        """Retorna o IP do domínio informado."""
        try:
            ip = socket.gethostbyname(self.domain)
            return ip
        except socket.gaierror:
            return "Unable to resolve IP"