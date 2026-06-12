"""
Имеется набор сообщений. Для данного сообщения написать программу с кодом Хемминга,
который позволит обнаруживать одиночную ошибку и исправлять ее. Для проверки привести
решение «вручную», в котором виден процесс построения кодов
"""
from Class1 import *


message = "00110000010010100"
print(f"Сообщение: {message}")

h = HammingCode(message)

code = h.encode()
print(f"Закодировано: {code}")

while True:
    try:
        mistake = int(input('Введите где должна быть ошибка '))
        if mistake > len(code) or mistake <= 0:
            print(f'Введите число в диапозоне 1 - {len(code)}')
            continue
        else:
            mistake = mistake - 1
            break
    except ValueError:
        print('Нверное значение')
        continue

code_list = list(code)
code_list[mistake] = '1' if code_list[mistake] == '0' else '0'
code_with_error = ''.join(code_list)
print(f"С ошибкой:    {code_with_error}")

decoded = h.decode(code_with_error)
print(f"\nРезультат: {decoded}")
