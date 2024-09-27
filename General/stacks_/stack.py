# Ejemplo de una pila en Python
class Stack():
    def __init__(self):
        self.items = []

    # Método para agregar un elemento a la pila
    def push(self, item):
        self.items.append(item)				

    # Método para eliminar un elemento de la pila
    def pop(self):
        return self.items.pop()

    # Método para verificar si la pila está vacía
    def is_empty(self):
        return self.items == []

    # Método para obtener el último elemento de la pila
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Método para obtener la pila
    def get_stack(self):
        return self.items


if __name__ == "__main__":
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    myStack.push("C")
    myStack.push("D")
    print(myStack.peek())