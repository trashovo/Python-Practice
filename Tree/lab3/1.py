"""
 Дано дерево поиска и корень дерева P1. Удалить в дереве вершину со значением
K. При замене содержимого удаляемой вершины использовать данные из ее левого поддерева.
После удаления вывести строку с описанием исходного дерева в следующем формате:
<дерево>::=((<левое
поддерево>)<вершина>(<правое
поддерево>))
|
((<левое
поддерево>)<вершина>) | (<вершина>(<правое поддерево>)) <вершина>::=<цифра><цифра> |
<цифра> <левое поддерево>::=<дерево> <правое поддерево>::=<дерево> Например,
"(((1)2((3)4))5(6(7)))". Пробелы в результирующей строке отсутствуют, ссылки на пустые
деревья никак не выводятся.
"""
from Class1 import *

while True:
    try:
        P1_val = int(input('Введите корень '))
        P1 = Node(P1_val)
        break
    except ValueError:
        print('Неверное значение')

while True:
    try:
        nums = list(map(int, input("Значения: ").split()))
        break
    except ValueError:
        print("Неверное значение")

root = P1
for x in nums:
    root.insert(x)

print(root.print_format())

if root is not None:
    while True:
        try:
            K = int(input("Какое число удалить? K = "))
            if K not in nums:
                print('Такого числа нету')
                continue
            else:
                root = root.delete(K)
                break
        except ValueError:
            print("Неверное значение K")

if root is not None:
    print(root.print_format())
else:
    print("Дерево пустое")