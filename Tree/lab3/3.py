"""
В первой строке текстового файла записаны целые числа, разделенные
пробелами. Создать дерево поиска, последовательно включая в него перечисленные в файле
числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив
для LR-поворот. Известно, что требуется не более одного такого поворота. Вывести корень
полученного дерева.
"""
from Class3 import *

try:
    with open("3input.txt", "r") as file:
        line = file.readline()
        nums = list(map(int, line.split()))
except FileNotFoundError:
    print('Ошибка чтения файла')
    exit()
except ValueError:
    print('Неверные значения')
    exit()

if nums:
    tree = AVLTree()
    root = None

    for num in nums:
        root = tree.insert(root, num)

    print(f"Корень исходного дерева поиска: {root.key}")

    root = tree.lr_rotate(root)

    print(f"Корень полученного АВЛ-дерева: {root.key}")