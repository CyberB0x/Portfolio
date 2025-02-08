import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import re

# Функция для генерации мета-тегов на основе URL
def generate_meta_tags(url):
    try:
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

        return {
            'title': title,
            'description': description,
            'keywords': keywords
        }
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные с URL: {e}")
        return None

# Функция для генерации мета-тегов на основе текста
def create_custom_meta_tags(text):
    description = text[:150] + '...' if text else 'Description not found'
    words = re.findall(r'\w+', text.lower())
    keywords = ', '.join(words[:10]) if words else 'Keywords not found'

    return {
        'title': 'Generated Title',
        'description': description,
        'keywords': keywords
    }

# Функция обработки ввода URL
def on_generate_url():
    url = url_entry.get()
    if url:
        meta_tags = generate_meta_tags(url)
        if meta_tags:
            title_var.set(meta_tags['title'])
            description_var.set(meta_tags['description'])
            keywords_var.set(meta_tags['keywords'])
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите URL!")

# Функция обработки ввода текста
def on_generate_text():
    text = text_entry.get("1.0", "end-1c")  # Получаем текст из многострочного поля
    if text:
        custom_meta_tags = create_custom_meta_tags(text)
        title_var.set(custom_meta_tags['title'])
        description_var.set(custom_meta_tags['description'])
        keywords_var.set(custom_meta_tags['keywords'])
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите текст!")

# Создаем основное окно
root = tk.Tk()
root.title("Генератор Мета-Тегов")

# Заголовок
header_label = tk.Label(root, text="Генератор Мета-Тегов", font=("Arial", 16))
header_label.pack(pady=10)

# Фрейм для URL
url_frame = tk.Frame(root)
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="Введите URL:", font=("Arial", 12))
url_label.pack(side="left", padx=10)

url_entry = tk.Entry(url_frame, width=50, font=("Arial", 12))
url_entry.pack(side="left")

url_button = tk.Button(url_frame, text="Генерировать для URL", font=("Arial", 12), command=on_generate_url)
url_button.pack(side="left", padx=10)

# Фрейм для текста
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

text_label = tk.Label(text_frame, text="Введите текст:", font=("Arial", 12))
text_label.pack(side="left", padx=10)

text_entry = tk.Text(text_frame, height=5, width=50, font=("Arial", 12))
text_entry.pack(side="left")

text_button = tk.Button(text_frame, text="Генерировать для текста", font=("Arial", 12), command=on_generate_text)
text_button.pack(side="left", padx=10)

# Места для вывода мета-тегов
result_frame = tk.Frame(root)
result_frame.pack(pady=20)

title_var = tk.StringVar()
description_var = tk.StringVar()
keywords_var = tk.StringVar()

title_label = tk.Label(result_frame, text="Title: ", font=("Arial", 12))
title_label.grid(row=0, column=0, sticky="w", padx=10)

title_output = tk.Label(result_frame, textvariable=title_var, font=("Arial", 12), width=50, anchor="w")
title_output.grid(row=0, column=1)

description_label = tk.Label(result_frame, text="Description: ", font=("Arial", 12))
description_label.grid(row=1, column=0, sticky="w", padx=10)

description_output = tk.Label(result_frame, textvariable=description_var, font=("Arial", 12), width=50, anchor="w")
description_output.grid(row=1, column=1)

keywords_label = tk.Label(result_frame, text="Keywords: ", font=("Arial", 12))
keywords_label.grid(row=2, column=0, sticky="w", padx=10)

keywords_output = tk.Label(result_frame, textvariable=keywords_var, font=("Arial", 12), width=50, anchor="w")
keywords_output.grid(row=2, column=1)

# Запуск основного цикла приложения
root.mainloop()
