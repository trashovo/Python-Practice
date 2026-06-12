def symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def check(matrix, n):
    errors = []

    if not matrix:
        errors.append("Матрица пуста")
        return errors

    if len(matrix) != n:
        errors.append(f"Неверное количество строк")

    for i, row in enumerate(matrix):
        if len(row) != n:
            errors.append(f"Ошибка в {i+1} строке")

    if not symmetric(matrix):
        errors.append("Матрица не является симметричной")

    return errors