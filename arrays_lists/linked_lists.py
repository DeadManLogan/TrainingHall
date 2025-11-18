class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        head = self.head
        current = head
        while current:
            print(current.value)
            current = current.next


linked1 = LinkedList()
linked1.insert_at_head(10)
linked1.insert_at_head(20)
linked1.insert_at_head(30)

linked1.print_list()