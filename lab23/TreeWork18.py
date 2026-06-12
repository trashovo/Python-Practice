"""
Дано бинарное дерево и корень дерева P1. Необходимо вывести второе
 максимальное значение в дереве. Решение должно иметь сложность по времени исполнения
 T(n) = O(log n), где n- число вершин в дереве.
"""
from Tree import *

P1_val = int(input('Введите корень '))
P1 = Node(P1_val)
print("Корень P1 =", P1.val)


while True:
    try:
        nums = list(map(int, input("Значения: ").split()))
        break
    except ValueError:
        print("Неверное значение")


for x in nums:
        P1.insert(x)

P1.levelorder()


second_max = P1.find_second_max()
if second_max is None:
    print("В дереве меньше 2 узлов")
else:
    print(f"Второе максимальное значение: {second_max}")
