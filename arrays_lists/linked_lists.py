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

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next     # save next node
            curr.next = prev          # reverse pointer
            prev = curr               # move prev forward
            curr = next_node          # move curr forward

        self.head = prev

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True  # cycle detected

        return False  # no cycle
    
    def nth_from_end(self, n):
        fast = self.head
        slow = self.head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.value
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        curr = self.head
        prev = None

        while curr:
            if curr.value in seen:
                prev.next = curr.next   # delete node
            else:
                seen.add(curr.value)
                prev = curr
            curr = curr.next

    def remove_duplicates_no_buffer(self):
        curr = self.head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.value == curr.value:
                    runner.next = runner.next.next  # delete
                else:
                    runner = runner.next
            curr = curr.next



linked = LinkedList()
linked.insert_at_tail(10)
linked.insert_at_tail(20)
linked.insert_at_tail(20)
linked.insert_at_tail(10)
linked.print_list()

print(linked.remove_duplicates_no_buffer())
linked.print_list()