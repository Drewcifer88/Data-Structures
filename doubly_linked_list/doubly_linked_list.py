"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if self.length == 0:
            # if there's nothing then when you add the node it will be the tail
            self.tail = new_node
        else:
            # if there's at least one element then there _was_ a head and we'll update it's prev
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length > 0:
            value = self.head
            self.head = self.head.next
            self.length -= 1
            if self.length > 0:
                self.head.prev = None
            else:
                print(self.tail)
                self.tail = None
                print(self.tail)
            return value.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        if self.length > 0:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length > 0:
            removed_node = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length = 0
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.length -= 1

            return removed_node.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node.prev == None:
            return
        elif node.next == None:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node.next == None:
            return
        elif node.prev == None:
            node.next.prev == None
            self.head = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
        elif node is self.tail:
            self.tail = self.tail.prev
        self.length -= 1
        node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head is None:
            return None

        maxNode = self.head.getValue()

        currentNode = self.head.getNext()

        while currentNode is not None:
            if currentNode.getValue() > maxNode:
                maxNode = currentNode.getValue()

            currentNode = currentNode.getNext()

        return maxNode
