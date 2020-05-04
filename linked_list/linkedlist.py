from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        """Adiciona um elemento na lista"""
        if self.head:
            # inserção quando a lista já possui elemetos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size += 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    def index(self, elem):
        """Retorna o índice do elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} is not in list")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head 
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.prox = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif elem == self.head.data:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f"{elem} is not in list")

    def __repr__(self):
        r = f"[ size = {self._size}, "
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        r += "None ]"
        return r

    def __str__(self):
        return self.__repr__()