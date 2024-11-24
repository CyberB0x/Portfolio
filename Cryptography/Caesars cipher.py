import tkinter as tk
from tkinter import messagebox
from turtledemo.penrose import start


# Функция для шифрования текста с использованием шифра Цезаря
def caesar_encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return ''.join(result)

# Функция для дешифрования текста с использованием шифра Цезаря
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Функция для обработки события шифрования
def encrypt_text():
    try:
        shift = int(shift_entry.get())  # Получаем сдвиг из поля ввода
        original_text = text_input.get("1.0", tk.END).strip()  # Получаем текст из поля ввода
        encrypted_text = caesar_encrypt(original_text, shift)  # Шифруем текст
        result_text.delete("1.0", tk.END)  # Очищаем поле с результатом
        result_text.insert(tk.END, encrypted_text)  # Вставляем зашифрованный текст в результат
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректный сдвиг (целое число).")

# Функция для обработки события дешифрования
def decrypt_text():
    try:
        shift = int(shift_entry.get())  # Получаем сдвиг из поля ввода
        encrypted_text = text_input.get("1.0", tk.END).strip()  # Получаем текст из поля ввода
        decrypted_text = caesar_decrypt(encrypted_text, shift)  # Дешифруем текст
        result_text.delete("1.0", tk.END)  # Очищаем поле с результатом
        result_text.insert(tk.END, decrypted_text)  # Вставляем расшифрованный текст в результат
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректный сдвиг (целое число).")

# Создаем основное окно
root = tk.Tk()
root.title("Шифратор и Дешифратор Цезаря")

# Создаем текстовое поле для ввода текста
text_input_label = tk.Label(root, text="Введите текст:")
text_input_label.pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Ввод сдвига
shift_label = tk.Label(root, text="Введите сдвиг (целое число):")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Кнопки для шифрования и дешифрования
encrypt_button = tk.Button(root, text="Шифровать", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Дешифровать", command=decrypt_text)
decrypt_button.pack()

# Поле для вывода зашифрованного или расшифрованного текста
result_label = tk.Label(root, text="Результат:")
result_label.pack()
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Запуск основного цикла приложения
root.mainloop()