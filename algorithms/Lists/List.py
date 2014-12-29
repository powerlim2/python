"""
Title: List data structure implementation in python
Author: Joon Lim <powerlim2@gmail.com>
Interpreter: Python 2.7

Note:
    - SinglyLinkedList is a Stack.
"""
from Node import Node


class LinkedList:
    """
    An unordered List implemented using Node class

    LinkedList API
    ----------------------------------------------
    push(item)          // add a new item in the beginning
    pop()               // remove the first item and print out
    add(item, before)   // add an item before a specific item
    remove(item)        // remove a specific item
    get(index)          // get item at the specific index
    index(item)         // get index for the specific item
    size()              // print out the number of items in the list
    search(item)        // check whether the item is in the list
    is_empty()          // check whether the list is empty
    """
    def __init__(self):
        self.head = None
        self.N = 0

    def __str__(self):
        return "{}".format(self.head)

    def is_empty(self):
        """
        check whether the list is empty
        """
        return self.head is None

    def push(self, item):
        """
        add a new item in the beginning
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.N += 1

        return self  # enable a chain call

    def pop(self):
        """
        remove the first item and print out
        """
        head = self.head
        value = head.get_value()
        self.head = head.get_next()
        self.N -= 1

        return value

    def size(self):
        """
        print out the number of items in the list
        """
        return self.N

    def search(self, item):
        """
        check whether the item is in the list
        """
        current = self.head
        found = False

        while current is not None and not found:
            if current.equals(item):
                found = True
            else:
                current = current.get_next()

        return found

    def index(self, item):
        """
        get item at the specific index
        """
        current = self.head
        found = False
        count = 0

        while current is not None and not found:
            if current.equals(item):
                found = True
            else:
                current = current.get_next()
                count += 1

        return count

    def get(self, index):
        """
        get item at the specific index
        """
        current = self.head
        count = index

        while count > 0:
            current = current.get_next()
            count -= 1

        return current.get_value()

    def add(self, item, before):
        """
        add an item before a specific item (inefficient)
        """
        current = self.head
        previous = None
        found = False

        while not found:
            if current.equals(before):
                found = True
            else:
                previous = Node(current.get_value(), previous)
                current = current.get_next()

        if previous is None:
            temp = Node(item, current)
        else:
            temp = Node(item, current)
            while previous is not None:
                temp = Node(previous.get_value(), temp)
                previous = previous.get_next()

        self.head = temp
        self.N += 1

        return self

    def remove(self, item):
        """
        remove a specific item (inefficient)
        """
        current = self.head
        previous = None
        found = False

        while not found:
            if current.equals(item):
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        self.N -= 1
        return self


def main():
    L = LinkedList()
    L.push(31).push(77).push(17).push(93).push(26).push(54)
    print L

    print(L.size())
    print(L.search(93))
    print(L.search(100))

    L.add(100, 17).add(110, 54)
    print(L.search(100))
    print(L.size())
    print L

    L.remove(54).remove(93).remove(31)
    print L.pop()
    print L.pop()
    print L
    print L.index(77)
    print L.get(2)

if __name__ == "__main__":
    main()