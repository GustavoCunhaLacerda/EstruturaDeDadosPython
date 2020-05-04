from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        """Insere um elemento na fila"""
        node = Node(elem)
        self._size += 1
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

    def pop(self):
        """Remove e retorna o elemento do inicio da fila"""
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        else:
            raise IndexError("The queue is empty")

    def peek(self):
        """Retorna o inicio sem remover"""
        if self.first:
            elem = self.first.data
            return elem
        else:
            raise IndexError("The queue is empty")

    def __len__(self):
        """Retorna o tamanho da fila"""
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = f"[ size = {self._size}; "
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + ", "
                pointer = pointer.next
            r += "None ]"
            return r
        return "Queue is empty"

    def __str__(self):
        return self.__repr__()
