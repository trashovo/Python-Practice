class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def levelorder(self):
        if not self:
            return
        queue = [self]
        while queue:
            next_queue = []
            for node in queue:
                print(node.data, end=" ")
                if node.prev:
                    next_queue.append(node.prev)
                if node.next:
                    next_queue.append(node.next)
            print()
            queue = next_queue


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def print_list(self):
        current = self.first
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

    def __len__(self):
        return self.size

    def sorted_list_to_bst(self):
        n = len(self)
        head_ptr = [self.first]

        def convert_recursive(n):
            if n <= 0:
                return None
            left = convert_recursive(n // 2)
            root = head_ptr[0]
            root.prev = left
            head_ptr[0] = head_ptr[0].next
            root.next = convert_recursive(n - 1 - (n // 2))
            return root

        return convert_recursive(n)