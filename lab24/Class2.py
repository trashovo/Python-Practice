class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.next_side = "left"

    def insert(self, key):
        if self.next_side == "left":
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
            self.next_side = "right"
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
            self.next_side = "left"
        return self

    def levelorder(self):
        if not self:
            return
        queue = [self]
        while queue:
            next_queue = []
            for node in queue:
                print(node.val, end=" ")
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            print()
            queue = next_queue


class TreeIterator:
    def __init__(self, root):
        self.stack = []
        self.current = root

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack and self.current is None:
            raise StopIteration

        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.right

        node_to_return = self.stack.pop()
        result_value = node_to_return.val

        self.current = node_to_return.left

        return result_value


class CameraSystem:
    def __init__(self):
        self.cameras = 0
        self.camera_positions = []
        self.root = None

    def solve(self, node):
        if self.root is None:
            self.root = node

        if not node:
            return 1

        left_state = self.solve(node.left)
        right_state = self.solve(node.right)

        if left_state == 0 or right_state == 0:
            self.cameras += 1
            self.camera_positions.append(node.val)
            return 2


        if left_state == 2 or right_state == 2:
            return 1

        if node == self.root:
            self.cameras += 1
            self.camera_positions.append(node.val)
            return 2

        return 0