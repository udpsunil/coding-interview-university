"""
Node to represent the value
"""


class Node:
    """
    Class that holds value and link to next element
    """

    def __init__(self, value):
        """
        Initialization
        :param value: value that can be stored in the node
        """
        self.value = value
        self.next = None
