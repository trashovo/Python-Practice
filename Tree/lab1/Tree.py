class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def build_tree(self, numbers):
        if not numbers:
            return self

        nodes = []
        nodes.append(self)
        for num in numbers:
            nodes.append(Node(num))

        for i in range(len(nodes)):
            left_id = 2 * i + 1
            right_id = 2* i + 2

            if left_id < len(nodes):
                nodes[i].left = nodes[left_id]
            if right_id < len(nodes):
                nodes[i].right = nodes[right_id]

        return nodes[0]

    def right_to_left(self, root):
        if root is None:
            return
        self.right_to_left(root.right)
        self.right_to_left(root.left)
        if root.left is None and root.right is None:
            print(root.val, end=" ")

    def insert(self, key):
        if key < self.val:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.val:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        return self

    def height(self):
        left_h = self.left.height() if self.left else 0
        right_h = self.right.height() if self.right else 0
        return 1 + max(left_h, right_h)

    def printGivenLevel(self, level):
        if level == 1:
            print(self.val, end=" ")
        else:
            if self.left:
                self.left.printGivenLevel(level - 1)
            if self.right:
                self.right.printGivenLevel(level - 1)

    def levelorder(self):
        h = self.height()
        for i in range(1, h + 1):
            self.printGivenLevel(i)
            print()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.inorder()

    def find_second_max(self):
        steps = 0
        parent = None
        current = self

        while current.right:
            parent = current
            current = current.right
            steps += 1

        if current.left:
            temp = current.left
            steps += 1
            while temp.right:
                temp = temp.right
                steps += 1
            print(f"Шагов сделано: {steps}")
            return temp.val

        print(f"Шагов сделано: {steps}")
        return parent.val if parent else None

