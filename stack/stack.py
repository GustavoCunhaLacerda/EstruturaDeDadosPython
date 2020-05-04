from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        """Insere um elemento na pilha"""
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1


    def pop(self):
        """Remove e retorna o elemento do topo da pilha"""
        if self.top:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            raise IndexError("the stack is empty")

    def peek(self):
        """Retorna o topo sem remover"""
        if self.top:
            return self.top.data
        else:
            raise IndexError("the stack is empty")

    def __len__(self):
        """Retorna o tamanho da pilha"""
        return self._size

    def __repr__(self):
        r = f"--\nsize = {self._size},\n->"
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        r += "None \n--"
        return r

    def __str__(self):
        return self.__repr__()
