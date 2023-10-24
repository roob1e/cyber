import socket
import subprocess

def scan_port(host, port):
    try:
        # Создаем сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.000001)

        # Пытаемся подключиться к порту
        result = s.connect_ex((host, port))

    
        if result == 0:
            print(f"Порт {port} на {host} открыт")
            o_ports.append(port)
        else:
            print(f'Порт {port} на {host} закрыт')

        s.close()
    except socket.error:
        print(f"Ошибка при соединении с портом {port} на {host}")


if __name__ == "__main__":
    target_host = "example.com"  
    target_ports = list(range(0, 30)) 
    o_ports = []

    for port in target_ports:
        scan_port(target_host, port)



print(o_ports)
if o_ports != []:
    close_q = input('Вы хотите закрыть ваш(и) открытый(е) порт(ы)? \n')
    close_q = close_q.lower()
    if (close_q == 'y') or (close_q == 'yes') or (close_q == 'да'):
        for op in o_ports:
            process = subprocess.Popen(f'netsh advfirewall firewall add rule dir=in action=block protocol=tcp localport={op} name=“Block1_TCP-{op}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
    else:
        exit()
elif o_ports == []:
    print(f'У вас нет открытых портов в диапазоне от {target_ports[0]} до {target_ports[-1]}')