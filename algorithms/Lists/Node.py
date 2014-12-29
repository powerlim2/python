"""
Title: Representation of the traditional node in Python
Author: Joon Lim <powerlim2@gmail.com>
Interpreter: Python 2.7
"""


class Node:
    def __init__(self, _value, _next=None):
        self.value = _value
        self.next = _next

    def __str__(self):
        """
        print the instance variables in JSON format
        """
        return "{'value':'%s', 'next':'%s'}" % (self.value, self.next)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, _value):
        self.value = _value
        return self

    def set_next(self, _next):
        self.next = _next
        return self

    def equals(self, item):
        return self.value == item


def main():
    n = Node("a")
    print n

if __name__ == "__main__":
    main()

