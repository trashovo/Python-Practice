class HammingCode:
    def __init__(self, data):
        self.data = data
        self.k = len(data)
        self.control_pos = self._control_positions()
        self.n = self.k + len(self.control_pos)

    def _control_positions(self):
        positions = []
        j = 1
        while j <= self.k + len(positions):
            positions.append(j)
            j *= 2
        return positions

    def encode(self):
        code = [0] * (self.n + 1)

        data_idx = 0
        for i in range(1, self.n + 1):
            if i in self.control_pos:
                continue
            code[i] = int(self.data[data_idx])
            data_idx += 1

        for p in self.control_pos:
            total = 0
            step = p
            start = p

            while start <= self.n:
                end_of_block = min(start + step, self.n + 1)

                for j in range(start, end_of_block):
                    total += code[j]

                start += step * 2

            code[p] = total % 2

        return ''.join(str(code[i]) for i in range(1, self.n + 1))

    def decode(self, received):
        code = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            code[i] = int(received[i - 1])

        error_pos = 0
        for p in self.control_pos:
            total = 0
            step = p
            start = p

            while start <= self.n:
                end_of_block = min(start + step, self.n + 1)

                for j in range(start, end_of_block):
                    if j != p:
                        total += code[j]
                start += step * 2

            if total % 2 != code[p]:
                error_pos += p

        if error_pos != 0:
            print(f"Ошибка на позиции {int(error_pos)}")
            code[error_pos] ^= 1

        result = []
        for i in range(1, self.n + 1):
            if i not in self.control_pos:
                result.append(str(code[i]))

        return ''.join(result)