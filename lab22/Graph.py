from collections import deque


class Graph:
    def __init__(self):
        self.n = 0
        self.adj_matrix = []
        self.graph = {}

    def load(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Файл не найден")
            return False

        if not lines:
            print('Файл пустой')
            return False

        self.n = int(lines[0].strip())
        self.adj_matrix = []

        if len(lines) - 1 != self.n:
            print(f"Неверное количество строк в матрице")
            return False

        for i in range(1, self.n + 1):
            row = list(map(int, lines[i].strip().split()))
            self.adj_matrix.append(row)

        self.build_graph()
        return True

    def build_graph(self):
        self.graph = {}
        for i in range(self.n):
            node = i + 1
            self.graph[node] = []
            for j in range(self.n):
                if self.adj_matrix[i][j] == 1:
                    self.graph[node].append(j + 1)

    def build_incidence(self):
        edges = []
        for i in range(self.n):
            for j in range(self.n):
                if i < j and self.adj_matrix[i][j] == 1:
                    edges.append((i, j))

        self.m = len(edges)
        self.incidence_matrix = [[0] * self.m for _ in range(self.n)]

        for idx, (v1, v2) in enumerate(edges):
            self.incidence_matrix[v1][idx] = 1
            self.incidence_matrix[v2][idx] = 1

        with open("Filename2", 'w') as f:
            f.write(f"{self.n} {self.m}\n")
            for row in self.incidence_matrix:
                f.write(' '.join(map(str, row)) + '\n')

    def get_adj_matrix(self):
        return self.adj_matrix

    def get_n(self):
        return self.n

    def get_nodes(self):
        return list(range(1, self.n + 1))

    def bfs_paths(self, start, goal):
        queue = deque([[start, [start]]])
        while queue:
            (vertex, path) = queue.popleft()
            for next_node in set(self.graph[vertex]) - set(path):
                if next_node == goal:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

    def shortest_path(self, start, goal):
        try:
            return next(self.bfs_paths(start, goal))
        except StopIteration:
            return None

    def route_search(self, K, L):
        nodes = self.get_nodes()
        result = []

        print(f"\nИз города {K} с менее чем {L} пересадками:")

        for target in nodes:
            if target == K:
                continue

            path = self.shortest_path(K, target)

            if path is not None:
                transfers = len(path) - 2
                if transfers < L:
                    result.append(target)

        result.sort()

        for target in result:
            path = self.shortest_path(K, target)
            transfers = len(path) - 2
            path_str = ' -> '.join(map(str, path))
            print(f"  В город {target}, путь: {path_str}, пересадок: {transfers}")

        if not result:
            print(f"-1")

        return result

    def route_all_search(self, K, K1, L):
        all_routes = []

        for path in self.bfs_paths(K, K1):
            transfers = len(path) - 2
            if transfers == L:
                all_routes.append(path)

        all_routes.sort()

        with open("Filename2", 'w') as f:
            if not all_routes:
                f.write("-1\n")
                return

            f.write(f"{len(all_routes)}\n")
            for route in all_routes:
                f.write(' -> '.join(map(str, route)) + '\n')