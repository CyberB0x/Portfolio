from flask import Flask, request
import os

app = Flask(__name__)

# Файл для сохранения IP-адресов
IP_FILE = 'ip_addresses.txt'


def save_ip(ip_address):
    """Сохраняет IP-адрес в файл."""
    with open(IP_FILE, 'a') as file:
        file.write(f"{ip_address}\n")


@app.route('/get_ip', methods=['GET'])
def get_ip():
    # Получаем IP-адрес из заголовка X-Forwarded-For или из remote_addr
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Если в заголовке несколько IP-адресов, берем первый
    if ip_address and ',' in ip_address:
        ip_address = ip_address.split(',')[0]

    # Сохраняем IP-адрес в файл
    save_ip(ip_address)

    return f"Ваш IP-адрес: {ip_address}"


if __name__ == '__main__':
    # Проверка на существование файла, чтобы избежать ошибок, если файл не существует
    if not os.path.exists(IP_FILE):
        with open(IP_FILE, 'w') as file:
            pass  # Создаем пустой файл, если его нет

    app.run(host='0.0.0.0', port=5000)  # Сервер будет слушать на всех интерфейсах
