"""Реализовать для бинарного дерева интерфейс итератора, который будет возвращать
значения элементов, находящихся в узлах дерева, в порядке "право-корень-лево".
Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать
запрещается."""
from Class2 import *


def main():
    print("Введите числа:")
    while True:
        try:
            nums = list(map(int, input().split()))
            if len(nums) == 0:
                print("Введите хотя бы одно число")
                continue
            break
        except ValueError:
            print("Неверное значение")

    root = None
    for x in nums:
        if root is None:
            root = Node(x)
        else:
            root.insert(x)

    print("\nДерево:")
    root.levelorder()

    print("Обход дерева итератором (Право-Корень-Лево):")

    iterator = TreeIterator(root)
    for value in iterator:
        print(value, end=" ")

if __name__ == "__main__":
    main()