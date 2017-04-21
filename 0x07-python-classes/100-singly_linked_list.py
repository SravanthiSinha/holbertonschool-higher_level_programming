#!/usr/bin/python3
"""
This is module 100-singly_linked_list

This module contains the definition of 2 classes:
Node and SinglyLinkedList
"""


class Node:
    """
    Creates type Node

    **parameters**
    data: private, must be an int
    next_node: private, must be a Node or None

    **methods**
    data(self)
    data(self, value)
    next_node(self)
    next_node(self, value)
    __init__(self, data, next=None)
    """
    def __init__(self, data, next_node=None):
        """
        instantiates a Node

        Arguments:
            data
            next_node: not required, must be a Node or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter for data attribute

        no arguments

        Returns:
            __data attribute
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        setter for data attribute

        Argument:
            value: must be an int
        """
        if not type(value) == int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        getter for next_node attribute

        no arguments

        Returns:
            __next_node attribute
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        setter fot next_node attribute

        Arguments
            value: must be Node or None type
        """
        if not (type(value) == Node or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list

    **parameters**
    head: private, a Node

    **methods**
    __init__(self)
    __str__(self)
    sorted_insert(self, value)
    """
    def __init__(self):
        """
        instantiates a singly linked  list

        no arguments
        """
        self.__head = None

    def __str__(self):
        """
        string representation of a singly linked list
        """
        node = self.__head
        string = ""
        if node is not None:
            while node.next_node is not None:
                string += "{:d}\n".format(node.data)
                node = node.next_node
            string += "{:d}".format(node.data)
        return (string)

    def sorted_insert(self, value):
        """
        insert a new value in a singly linked list by increasing value

        Argument:
            value: must be an int
        """
        new = Node(value)
        node = self.__head
        if node is None:
            self.__head = new
            return

        if new.data < node.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (node.next_node is not None) and node.next_node.data <= new.data:
                node = node.next_node
        new.next_node = node.next_node
        node.next_node = new
        return
