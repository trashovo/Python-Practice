"""Дано бинарное дерево и корень P1. Вывести листья справа налево"""
from Tree import *

while True:
    P1_val = input('Введите корень ')
    if P1_val == '':
        print('Корень не может быть пустой')
        continue
    else:
        P1 = Node(P1_val)
        break

print("Корень P1 =", P1.val)

while True:
    numbers = input('Введите значения: ').split()
    if not numbers:
        print('Вы ничего не ввели')
        continue
    else:
        break
root = P1.build_tree(numbers)

print("\nДерево:")
root.levelorder()

print("\nЛистья справа налево:")
root.right_to_left(root)
