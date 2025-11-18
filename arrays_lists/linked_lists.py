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

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        head = self.head
        current = head
        while current:
            print(current.value)
            current = current.next

    def delete_value(self, target):
        if not self.head:
            return
    
        # special case: delete the head
        if self.head.value == target:
            self.head = self.head.next
            return

        prev = None
        curr = self.head

        while curr:
            if curr.value == target:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


linked1 = LinkedList()
linked1.insert_at_head(10)
linked1.insert_at_head(20)
linked1.insert_at_tail(30)
linked1.insert_at_tail(40)

linked1.delete_value(10)

linked1.print_list()