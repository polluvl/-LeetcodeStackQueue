class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            raise ValueError
        head_return = self.head
        self.head = self.head.next
        return head_return.data

    def peek(self):
        return self.head.data

    def push(self, x):
        if self.head:
            temp = self.head
            self.head = Node(x)
            self.head.next = temp
        else:
            self.head = Node(x)

    def __len__(self):
        counter = 0
        if self.head:
            temp = self.head
            while temp:
                counter += 1
                temp = temp.next
        return counter


class MyQueue(object):

    def __init__(self):
        self.start = Stack()
        self.end = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.start.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.end.is_empty():
            while not self.start.is_empty():
                self.end.push(self.start.pop())
        if self.end.is_empty():
            raise ValueError
        el_return = self.end.pop()
        return el_return

    def peek(self):
        """
        :rtype: int
        """
        if self.end.is_empty():
            while not self.start.is_empty():
                self.end.push(self.start.pop())
        if self.end.is_empty():
            raise ValueError
        el_return = self.end.peek()
        return el_return


    def empty(self):
        """
        :rtype: bool
        """
        return self.start.is_empty() and self.end.is_empty()

