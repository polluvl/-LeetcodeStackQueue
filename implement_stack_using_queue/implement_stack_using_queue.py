'''stack of 2 queues'''
class Node:
    """a class of a node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """queue class (FIFO)
    """
    def __init__(self):
        self.head = None

    def add(self, x):
        """a method to add an el to the end of the queue

        Args:
            x (_type_): _description_
        """
        if self.head is None:
            self.head = Node(x)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(x)

    def pop(self):
        """a method to pop the first element from the queue

        Raises:
            ValueError: if the queue is empty or head is not defined

        Returns:
            _type_: _description_
        """
        if self.head is None:
            raise ValueError
        temp = self.head
        self.head = self.head.next
        return temp.data

    def is_empty(self):
        """a method to check if the queue is empty

        Returns:
            _type_: _description_
        """
        return self.head is None

    def peek(self):
        """a method to peek the first element from the queue

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if self.head:
            return self.head.data
        raise ValueError


class MyStack:
    """stack class (LIFO)
    """
    def __init__(self):
        self.inner = Queue()
        self.outer = Queue()

    def push(self, x):
        """Pushes element x to the top of the stack.

        Args:
            x (_type_): _description_
        """
        self.inner.add(x)

    def pop(self):
        """Removes the element on the top of the stack and returns it.
        """
        counter = 0
        if self.inner.is_empty():
            raise ValueError
        else:
            while not self.inner.is_empty():
                counter += 1
                self.outer.add(self.inner.pop())
            for i in range(1, counter):
                self.inner.add(self.outer.pop())
        return self.outer.pop()

    def top(self):
        """Returns the element on the top of the stack.
        """
        counter = 0
        if self.inner.is_empty():
            raise ValueError
        while not self.inner.is_empty():
            counter += 1
            self.outer.add(self.inner.pop())
        for i in range(counter-1):
            self.inner.add(self.outer.pop())
        toreturn = self.outer.pop()
        self.inner.add(toreturn)
        return toreturn

    def empty(self):
        """Returns true if the stack is empty, false otherwise.
        """
        return self.inner.is_empty() and self.outer.is_empty()
