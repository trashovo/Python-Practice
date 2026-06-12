from Class4 import *

try:
    with open("4input.txt", "r") as file:
        line = file.readline()
        nums = list(map(int, line.split()))
except FileNotFoundError:
    print('Ошибка чтения файла')
    exit()
except ValueError:
    print('Неверные значения')
    exit()

if nums:
    bst = BinarySearchTree()

    for num in nums:
        bst.root = bst.insert(bst.root, num)

    print(f"Корень дерева поиска: {bst.root.key}")

    output = []
    bst.post_order(bst.root, output)
    print(f"Концевой обход: {' '.join(output)}")