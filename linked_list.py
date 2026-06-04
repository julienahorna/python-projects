class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c

new_head = reverse(a)

node = new_head
while node :
    print(node.value)
    node = node.next
