class HuffmanCode:
    class Node:
        def __init__(self, freq, symbol=None, left=None, right=None):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right

    def __init__(self, text):
        self.text = text
        self.freq = {}
        self.codes = {}
        self.root = None

    def count_frequencies(self):
        for ch in self.text:
            self.freq[ch] = self.freq.get(ch, 0) + 1

    def print_freq(self):
        print("Частоты символов:")
        for ch, f in sorted(self.freq.items(), key=lambda x: -x[1]):
            name = 'пробел' if ch == ' ' else ch
            print(f"  '{name}': {f}")
        print()

    def build_tree(self):
        nodes = []
        for ch, f in self.freq.items():
            nodes.append(self.Node(freq=f, symbol=ch))

        nodes.sort(key=lambda x: x.freq)

        while len(nodes) > 1:
            left = nodes.pop(0)
            right = nodes.pop(0)

            parent = self.Node(freq=left.freq + right.freq, symbol=None, left=left, right=right)

            nodes.append(parent)
            nodes.sort(key=lambda x: x.freq)

        self.root = nodes[0]


    def generate_codes(self):
        def get_codes(node, code):
            if node.symbol is not None:
                self.codes[node.symbol] = code
            else:
                get_codes(node.left, code + "0")
                get_codes(node.right, code + "1")

        get_codes(self.root, "")


    def print_codes(self):
        print("Коды символов:")
        for ch, code in sorted(self.codes.items(), key=lambda x: len(x[1])):
            name = 'пробел' if ch == ' ' else ch
            print(f"  '{name}': {code}")
        print()


    def print_result(self):
        uniform = len(self.text) * 4
        huffman = sum(len(self.codes[ch]) for ch in self.text)

        print(f"Длина текста: {len(self.text)} символов")
        print(f"Равномерный код: {uniform} бит")
        print(f"Код Хаффмана: {huffman} бит")
        print(f"Экономия: {uniform - huffman} бит")

    def run(self):
        self.count_frequencies()
        self.print_freq()
        self.build_tree()
        self.generate_codes()
        self.print_codes()
        self.print_result()