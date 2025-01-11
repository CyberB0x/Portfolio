import requests
from bs4 import BeautifulSoup
"""
Автоматизация мониторинга цен
Автор: Arslonbek Erkinov
Версия: 1.1
"""

# URL для мониторинга цен
url = "<Your url>"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Поиск элемента с ценой
price_elements = soup.find_all("Your html tag")
if price_elements:
   for price_element in price_elements:
       price = price_element.text.strip()
       print(f"Цена товара: {price}")
else:
   print("Цена не найдена")