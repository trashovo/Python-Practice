"""
Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=25, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
городов, в которые из города K можно долететь менее чем с L пересадками. Перечислите
номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
таких городов нет, выведите число (-1).
"""
from Graph import *


def main():

    graph = Graph()
    if graph.load("Filename3"):

        adj_matrix = graph.get_adj_matrix()
        n = graph.get_n()

        errors = check(adj_matrix, n)

        if errors:
            for error in errors:
                print(error)
                return

        while True:
            try:
                K = int(input('Из какого города: '))
                if K < 1 or K > graph.get_n():
                    print(f'Город должен быть от 1 до {graph.get_n()}')
                    continue
                break
            except ValueError:
                print('Неверное значение')

        while True:
            try:
                L = int(input('Меньше скольки пересадок: '))
                if L < 0:
                    print('Количество пересадок не может быть отрицательным')
                    continue
                break
            except ValueError:
                print('Неверное значение')

        graph.route_search(K, L)


if __name__ == "__main__":
    main()