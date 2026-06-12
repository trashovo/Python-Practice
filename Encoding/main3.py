"Столбчатый шифр транспонирования"
from Class3 import *

while True:
    text = input('Введите текст ')
    if text == '':
        print('Введите текст')
        continue
    else:
        break

while True:
    key = input('Введите ключ ')
    if key == '':
        print('Введите ключ')
        continue
    else:
        break


cipher = ColumnarCipher(key)

print(f"Текст: {text}")
print(f"Ключ: {key}\n")

enc = cipher.encrypt(text)
print(f"Зашифровано: {enc}\n")

while True:
    text1 = input('Введите текст ')
    if text == '':
        print('Введите текст')
        continue
    else:
        break

while True:
    key1 = input('Введите ключ ')
    if key == '':
        print('Введите ключ')
        continue
    else:
        break

decode  = ColumnarCipher(key1)
dec = decode.decrypt(text1)
print(f"Расшифровано: {dec}")