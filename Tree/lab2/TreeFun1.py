""""Преобразовать двусвязный список в бинарное дерево поиска без использования
дополнительной памяти (создания новых объектов). Корнем дерева должен стать элемент
списка, находящийся в его середине, а само дерево должно иметь наименьшую возможную
высоту. При преобразовании поля left и right узлов бинарного дерева рассматриваются
эквивалентными полям prev и next узлов двусвязного списка. Вывести исходный список и
получившееся дерево"""
from Class1 import *


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

    dll = DoublyLinkedList()
    for x in nums:
        dll.append(x)

    print("Двусвязный список")
    dll.print_list()

    tree_root = dll.sorted_list_to_bst()

    print("Дерево:")
    tree_root.levelorder()

if __name__ == "__main__":
    main()