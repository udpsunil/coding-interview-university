"""
Class that implements a Linked list with all the required operations
"""
from work.node import Node


class LinkedList:
    """Linked List Class"""

    def __init__(self, head=None):
        """
        Initialize head index of linked list with None (Empty Linked List)
        """
        self.head = head
        self.length = 1 if head else 0

    def __str__(self):
        current = self.head
        # if there are elements in the linked list accumulate them in a list to print them
        if current is not None:
            temp = []
            while current is not None:
                temp.append(str(current.value))
                current = current.next
            return "Linked List:"+" ".join(temp)
        # else print a message
        else:
            return "List is Empty"

    def append(self, node):
        """
        Append given node at the end of linked list
        :param node: Node with a value
        :type node: Node
        :return: None
        """
        current = self.head
        if current is not None:
            current = self._reach_end(current)
            current.next = node
            self.length += 1
        else:
            self.head = node

    def insert(self, node, position):
        if position == 0:
            node.next = self.head
            self.head = node
            self.length += 1
        current = self.head
        if current is not None:
            if position <= self.length:
                current = self._reach_position(current, position)
                temp = current.next
                current.next = node
                node.next = temp
                self.length += 1
        else:
            if position == 0:
                self.head = current

    def delete(self, value):
        pass

    def get_position(self, position):
        """
        Get value at position
        :param position: position inside the list
        :type position: int
        :return: value or None
        """
        if position > self.length + 1:
            return None
        else:
            current = self.head
            if current is not None:
                current = self._reach_position(current, position)
            return current

    def _reach_end(self, current):
        """
        Return reference of last entry assuming at least one element exists
        :return: object
        """
        if current.next is not None:
            while current.next is not None:
                current = current.next
            return current
        else:
            return current

    def _reach_position(self, current, position):
        count = 1
        while current is not None:
            if count >= position:
                return current
            current = current.next
            count += 1
        return current


if __name__ == "__main__":
    node_0 = Node(0)
    linked_list = LinkedList(node_0)
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    print(linked_list)
    linked_list.append(node_1)
    print(linked_list)
    linked_list.append(node_2)
    print(linked_list)
    linked_list.append(node_3)
    print(linked_list)
    print(linked_list.get_position(3).value)
    print(linked_list.get_position(2).value)
    print(linked_list.get_position(1).value)
    print(linked_list.get_position(0).value)
    linked_list.insert(node_4,4)
    print(linked_list)
    print(linked_list.length)
