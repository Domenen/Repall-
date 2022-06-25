


class Node(object):
    """Ноды , построение"""
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
        
    def __str__(self):
        return f"[Node with value {self.value}]"


def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur)
        cur = cur.next

def reverse_list(head):
    """
        Реверс Нода который уже есть
    """
    current = head
    prev = None
    while current is not None:
        nxt = current.next
        current.next = prev

        prev = current
        current = nxt
    head = prev
    return head


h, a, b, c, d = Node(1), Node(2), Node(3), Node("текста"), Node(5)
h.next = a
a.next = b
b.next = c
c.next = d
print_linked_list(h)

h = reverse_list(h)
print_linked_list(h)