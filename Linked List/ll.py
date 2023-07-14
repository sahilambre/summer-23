class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

# node1 = Node(10)

# print(node1)


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


LL1 = LinkedList()
LL1.add_beginning(20)
LL1.add_beginning(10)
LL1.print_LL()

