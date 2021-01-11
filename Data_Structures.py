"""
Stack

Stack is First In, Last Out

"""


from collections import deque


class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def length(self):
        return self.len_stack


"""
Queue

Queue is First in, First Out

"""


class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]
        return "The Queue is Empty"


q = Queue()
print(q.front())


class Deque:

    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1


d = deque()
d.append(1)  # adiciona do lado direito
d.appendleft(2)  # adiciona do lado esquerdo
d.append(3)
d.append(4)

# 4, 2, 1, 3

d.pop()  # remove do lado direito
d.popleft()  # remove do lado esquerdo

d.remove(num)  # remove o numero


""" 

Linked List


"""


class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
