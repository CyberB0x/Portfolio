import requests
from bs4 import BeautifulSoup
import re

def generator_meta_tags(url):
    # Получаем HTML страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получаем title
    title = soup.title.string if soup.title else 'Title not found'

    # Получаем описание (meta description)
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'] if description_tag else 'Description not found'

    # Получаем ключевые слова (meta keywords)
    keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
    keywords = keywords_tag['content'] if keywords_tag else 'Keywords not found'

    # Генерация мета тегов
    meta_tags = {
        'title': title,
        'description': description,
        'keywords': keywords
    }

    return meta_tags


def create_custom_meta_tags(text):
    # Используем текст для создания кастомных мета-тегов (например, по первому абзацу или ключевым словам)
    # Простой пример: берем первые 150 символов текста для description
    description = text[:150] + '...'

    # Простой пример для ключевых слов (берем первые несколько значений)
    words = re.findall(r'\w+', text.lower())
    keywords = ', '.join(words[:10])

    return {
        'title': 'Generated Title',
        'description': description,
        'keywords': keywords
    }


# Пример использования
url = 'https://example.com'  # Замените на нужный URL
meta_tags = generator_meta_tags(url)
print(f"Title: {meta_tags['title']}")
print(f"Description: {meta_tags['description']}")
print(f"Keywords: {meta_tags['keywords']}")

# Если нужно создать мета-теги для текста
text = "Python programming is fun and versatile. Python is a powerful language for web development."
custom_meta_tags = create_custom_meta_tags(text)
print(f"Custom Title: {custom_meta_tags['title']}")
print(f"Custom Description: {custom_meta_tags['description']}")
print(f"Custom Keywords: {custom_meta_tags['keywords']}")