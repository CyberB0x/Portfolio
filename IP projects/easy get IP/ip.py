import requests


def get_location_by_ip(ip_address):
    # Ваш токен API из ipinfo.io
    token = 'token'  # Замените на ваш токен API

    # Используем токен для запроса
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location_info = {
            'IP-адрес': data.get('ip'),
            'Город': data.get('city'),
            'Регион': data.get('region'),
            'Страна': data.get('country'),
            'Широта и Долгота': data.get('loc')  # loc содержит координаты в формате "широта,долгота"
        }
        return location_info
    else:
        return {"error": "Не удалось получить данные"}


# Пример использования
ip_address = '78.171.183.87'  # Замените на интересующий вас IP-адрес
location_info = get_location_by_ip(ip_address)

# Выводим информацию
if 'error' not in location_info:
    print(f"IP-адрес: {location_info['IP-адрес']}")
    print(f"Город: {location_info['Город']}")
    print(f"Регион: {location_info['Регион']}")
    print(f"Страна: {location_info['Страна']}")
    print(f"Широта и Долгота: {location_info['Широта и Долгота']}")
else:
    print(location_info['error'])
