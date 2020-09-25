import socket

# Este script faz uma varredura e verifica quais portas estão abertas na rede.


def portscan(porta):
    target = '192.168.0.1'

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scann = sock.connect_ex((target, porta))

        if scann == 0:
            print(f'A porta {porta} está aberta!')
            sock.close()
        else:
            print(f'A porta {porta} está fechada!')

    except:
        return False


# Parametros para iniciar a varredura.
inicio = int(input('Porta inicial: '))
fim = int(input('Porta Final: '))

# Percorre todas as portas indicadas e mostra quais estão abertas e fechadas.
# chama a funcão PORTSCAN e inicia o procedimento.
for port in range(inicio, fim):
    result = portscan(port)
