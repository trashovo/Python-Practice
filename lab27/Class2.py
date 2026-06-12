class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if self.val >= 0:
            return False

        if self.left is None:
            self.left = Node(key)
            return True

        if self.left.val < 0:
            if self.left.insert(key):
                return True

        if self.right is None:
            self.right = Node(key)
            return True

        if self.right.val < 0:
            if self.right.insert(key):
                return True

        return False

    def copy_and_optimize(self):
        new_node = Node(self.val)

        if self.left is not None:
            new_node.left = self.left.copy_and_optimize()
        if self.right is not None:
            new_node.right = self.right.copy_and_optimize()

        if new_node.val == -1:
            if new_node.left is not None and new_node.left.val == 0:
                return new_node.right
            if new_node.right is not None and new_node.right.val == 0:
                return new_node.left

        elif new_node.val == -2:
            if new_node.right is not None and new_node.right.val == 0:
                return new_node.left

        elif new_node.val == -3:
            if (new_node.left is not None and new_node.left.val == 0) or (new_node.right is not None and new_node.right.val == 0):
                return Node(0)

        elif new_node.val == -4:
            if new_node.left is not None and new_node.left.val == 0:
                if new_node.right is not None and new_node.right.val != 0:
                    return Node(0)

        return new_node

    def to_string(self):
        mapping = {-1: '+', -2: '-', -3: '*', -4: '/'}

        if self.val >= 0:
            return str(self.val)

        left_str = self.left.to_string() if self.left is not None else ""
        right_str = self.right.to_string() if self.right is not None else ""
        op_str = mapping.get(self.val, "")

        return f"({left_str}{op_str}{right_str})"