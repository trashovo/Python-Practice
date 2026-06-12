class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        return self

    def find_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def delete(self, key):
        if key < self.key:
            if self.left is not None:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right is not None:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right

            max_left = self.left.find_max()
            self.key = max_left.key
            self.left = self.left.delete(max_left.key)

        return self

    def to_string(self):
        left_str = self.left.to_string() if self.left is not None else ""
        right_str = self.right.to_string() if self.right is not None else ""

        if left_str and right_str:
            return f"({left_str}){self.key}({right_str})"
        elif left_str:
            return f"({left_str}){self.key}"
        elif right_str:
            return f"{self.key}({right_str})"
        else:
            return f"{self.key}"

    def print_format(self):
        return f"({self.to_string()})"