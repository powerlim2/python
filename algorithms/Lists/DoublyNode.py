"""
Title: Representation of the traditional doubly node in Python
Author: Joon Lim <powerlim2@gmail.com>
Interpreter: Python 2.7
"""


class DoublyNode:
    def __init__(self, _value, _previous=None, _next=None):
        self.value = _value
        self.previous = _previous
        self.next = _next

    def __str__(self):
        """
        print the instance variables in JSON format
        """
        return "{'value':'%s', 'previous':'%s', 'next':'%s'}" % (self.value, self.previous, self.next)

    def get_value(self):
        return self.value

    def get_previous(self):
        return self.previous

    def get_next(self):
        return self.next

    def set_value(self, _value):
        self.value = _value
        return self

    def set_previous(self, _value):
        self.previous = _value
        return self

    def set_next(self, _next):
        self.next = _next
        return self

    def equals(self, item):
        return self.value == item


def main():
    d = DoublyNode("a")
    print d

if __name__ == "__main__":
    main()

