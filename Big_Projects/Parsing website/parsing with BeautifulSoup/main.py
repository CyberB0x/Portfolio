import requests
from bs4 import BeautifulSoup
"""
Парсинг данных с помощью BeautifulSoup
Автор: Arslonbek Ekinov 
Версия: 1.1
"""
# URL для парсинга
url = "<Your URL>"

# Отправка запроса к сайту
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Извлечение данных
titles = soup.find_all("div")  # Ищем заголовки

for title in titles:
    print(title.text)
