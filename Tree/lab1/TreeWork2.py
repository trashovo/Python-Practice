"""
Дано число N (> 0) и набор из N чисел. Отсортировать исходный набор чисел,
 создав для него бинарное дерево. Вывести корень P1 полученного дерева, а также
 отсортированный набор чисел (для вывода набора чисел выполнить перебор вершин дерева в
 инфиксном порядке)
"""
from Tree import *

while True:
    try:
        N = int(input("N = "))
        if N < 0:
            print('N не может быть меньше 0')
            continue
        break
    except ValueError:
        print('Неверное значение')

while True:
    try:
        nums = list(map(int, input("Значения: ").split()))
        if len(nums) == N:
            break
        else:
            print(f"Неверное количество чисел")
    except ValueError:
        print("Неверное значение")


root = None
for x in nums:
    if root is None:
        root = Node(x)
    else:
        root.insert(x)

root.levelorder()

print(f"\nКорень P1 = {root.val}")

root.inorder()
