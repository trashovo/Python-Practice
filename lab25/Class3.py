class ColumnarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        text = text.replace(" ", "")

        cols = len(self.key)
        rows = (len(text) + cols - 1) // cols

        matrix = []
        for i in range(rows):
            matrix.append([''] * cols)

        index = 0
        for row in range(rows):
            for col in range(cols):
                if index < len(text):
                    matrix[row][col] = text[index]
                    index += 1

        self.print_(matrix, rows, cols)

        order = []
        for symbol in self.key:
            order.append(int(symbol) - 1)

        result = []
        for col in order:
            for row in range(rows):
                if matrix[row][col] != '':
                    result.append(matrix[row][col])

        return ''.join(result)

    def decrypt(self, text):
        cols = len(self.key)
        rows = (len(text) + cols - 1) // cols

        last_row_cols = len(text) % cols
        if last_row_cols == 0:
            last_row_cols = cols

        col_heights = []
        for col in range(cols):
            if col < last_row_cols:
                col_heights.append(rows)
            else:
                col_heights.append(rows - 1)

        order = []
        for symbol in self.key:
            order.append(int(symbol) - 1)

        matrix = []
        for i in range(rows):
            matrix.append([''] * cols)

        index = 0
        for col in order:
            for row in range(col_heights[col]):
                matrix[row][col] = text[index]
                index += 1

        self.print_(matrix, rows, cols)

        result = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != '':
                    result.append(matrix[row][col])

        return ''.join(result)


    def print_(self, matrix, rows, cols):
        for k in self.key:
            print(f" {k} ", end="")
        print()
        for row in range(rows):
            for col in range(cols):
                val = matrix[row][col] if matrix[row][col] else '_'
                print(f" {val} ", end="")
            print()
        print()
