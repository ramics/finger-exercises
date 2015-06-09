import Functions

class LinkedList:
    """
    Incomplete definition of a linked list.
    """

    class Node:
        """
        A linked list node.
        """

        def __init__(self, value, next_node = None):
            self.value = value
            self.next = next_node

        def __str__(self):
            return str(self.value)

    def __init__(self, head = None):

        self.head = head

    def insert(self, value):

        self.head = self.Node(value, self.head)

    def __str__(self):

        return ', '.join(str(x.value) for x in Functions.fixed_point(
            lambda p:p.next, self.head, None
        ))


    

    def reverse(self):

        cur_node = None
        next_node = self.head

        while next_node is not None:

            temp = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = temp

        self.head = cur_node

