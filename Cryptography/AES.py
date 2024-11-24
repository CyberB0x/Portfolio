from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Генерация случайного ключа и IV (Initialization Vector)
def generation_key():
    key = os.urandom(32) # 256-битный ключ для AES
    iv = os.urandom(16) # 128-битный IV
    return key, iv

# Шифрование текста
def encrypt(text, key, iv):
    # Преобразуем строку в байты
    data = text.encode('utf-8')

    # Добавляем padding, чтобы длина данных была кратна 128 битам (16 байтов)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Создаем объект Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Шифруем данные
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return encrypted

# Дешифрование текста
def decrypt(encrypted_data, key, iv):
    # Создаем объект Cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Дешифруем данные
    decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

    # Убираем padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

    return decrypted_data.decode('utf-8')

# Пример использования
if __name__ == "__main__":
    # Генерация ключа и IV
    key, iv = generation_key()

    # Текст для шифрования
    text = "Hello, this is a secret message!"

    # Шифруем
    encrypted = encrypt(text, key, iv)
    print("Зашифрованный текст:", encrypted.hex())

    # Дешифруем
    decrypted = decrypt(encrypted, key, iv)
    print("Дешифрованный текст:", decrypted)


"""
Как это работает:
Шифрование: мы превращаем текст в байты, добавляем padding и шифруем с использованием алгоритма AES.
Дешифрование: восстанавливаем исходные данные, убирая padding после дешифрования.
"""