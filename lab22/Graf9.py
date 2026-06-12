"""
Юный путешественник решил изучить схему авиационного сообщения Схема
 авиационного сообщения задана в текстовом файле с именем FileName1. в виде матрицы
 смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
 авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
 имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить сколько
 есть маршрутов из города К1 в город К2 с L пересадками. В файл с именем FileName2 в
 первой строке выведите число таких маршрутов, а в следующих строках перечислите все
 такие маршруты в лексикографическом порядке. Маршрут задается перечислением
номеров городов, нумерация городов идет с 1. Если таких маршрутов нет, выведите число
 (-1).
"""
from Graph import Graph
from check import check


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
                K1 = int(input('В какой город: '))
                if K < 1 or K > graph.get_n():
                    print(f'Город должен быть от 1 до {graph.get_n()}')
                    continue
                elif K1 == K:
                    print("K1 не может быть равен K")
                    continue
                break
            except ValueError:
                print('Неверное значение')

        while True:
            try:
                L = int(input('Сколько пересадок: '))
                if L < 0:
                    print('Количество пересадок не может быть отрицательным')
                    continue
                break
            except ValueError:
                print('Неверное значение')

        graph.route_all_search(K, K1, L)


if __name__ == "__main__":
    main()