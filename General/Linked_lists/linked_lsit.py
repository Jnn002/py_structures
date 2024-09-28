class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Inicializa el siguiente nodo como None

class LinkedList:
    def __init__(self):
        self.head = None  # Inicializa la cabeza de la lista como None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)  # Imprime el dato del nodo actual
            cur_node = cur_node.next  # Avanza al siguiente nodo

    def append(self, data):
        new_node = Node(data)  # Crea un nuevo nodo

        if self.head is None:
            self.head = new_node  # Si la lista está vacía, el nuevo nodo es la cabeza
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Encuentra el último nodo
        last_node.next = new_node  # Añade el nuevo nodo al final

    def prepend(self, data):
        new_node = Node(data)  # Crea un nuevo nodo
        new_node.next = self.head  # El nuevo nodo apunta a la antigua cabeza
        self.head = new_node  # El nuevo nodo se convierte en la cabeza

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)  # Crea un nuevo nodo
        new_node.next = prev_node.next  # El nuevo nodo apunta al siguiente del nodo previo
        prev_node.next = new_node  # El nodo previo apunta al nuevo nodo

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next  # Si el nodo a eliminar es la cabeza, actualiza la cabeza
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next  # Encuentra el nodo a eliminar

        if cur_node is None:
            return 

        prev.next = cur_node.next  # El nodo previo apunta al siguiente del nodo a eliminar
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next  # Si la posición es 0, actualiza la cabeza
                cur_node = None
                return

            prev = None
            count = 1
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1  # Encuentra el nodo en la posición dada

            if cur_node is None:
                return 

            prev.next = cur_node.next  # El nodo previo apunta al siguiente del nodo a eliminar
            cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1  # Incrementa el contador por cada nodo
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)  # Llama recursivamente y suma 1 por cada nodo

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next  # Encuentra el primer nodo

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next  # Encuentra el segundo nodo

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2  # Actualiza el siguiente del nodo previo al primer nodo
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1  # Actualiza el siguiente del nodo previo al segundo nodo
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next  # Intercambia los siguientes de los nodos

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev  # Invierte el enlace

            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")

            prev = cur 
            cur = nxt  # Avanza al siguiente nodo
        self.head = prev  # Actualiza la cabeza

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev  # Invierte el enlace
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)  # Llama a la función recursiva

    def merge_sorted(self, llist):
        p = self.head 
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s  # Inicializa la nueva cabeza
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next  # Elimina el nodo duplicado
                cur = None
            else:
                dup_values[cur.data] = 1  # Marca el valor como encontrado
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n, method):
        if method == 1:
            total_len = self.len_iterative()
            cur = self.head 
            while cur:
                if total_len == n:
                    return cur.data  # Devuelve el dato del nodo en la posición n desde el final
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            p = self.head
            q = self.head

            count = 0
            while q:
                count += 1
                if(count >= n):
                    break
                q = q.next

            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head 
            q = self.head 
            prev = None 
            count = 0

            while p and count < k:
                prev = p
                p = p.next 
                q = q.next 
                count += 1  # Encuentra el nodo en la posición k
            p = prev
            while q:
                prev = q 
                q = q.next 
            q = prev 

            q.next = self.head  # Conecta el último nodo con la cabeza
            self.head = p.next  # Actualiza la cabeza
            p.next = None  # Desconecta el nodo en la posición k

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1  # Incrementa el contador si el dato coincide
            cur = cur.next
        return count 

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0 
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)  # Suma 1 si el dato coincide
        else:
            return self.count_occurences_recursive(node.next, data)

    def is_palindrome_1(self):
        s = ""
        p = self.head 
        while p:
            s += p.data  # Construye una cadena con los datos de los nodos
            p = p.next
        return s == s[::-1]  # Comprueba si la cadena es un palíndromo

    def is_palindrome_2(self):
        p = self.head 
        s = []
        while p:
            s.append(p.data)  # Almacena los datos en una lista
            p = p.next
        p = self.head
        while p:
            data = s.pop()  # Compara los datos con los de la lista
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_3(self):
        if self.head:
            p = self.head 
            q = self.head 
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1  # Almacena los nodos en una lista
            q = prev[i-1]

            count = 1

            while count <= i // 2 + 1:
                if prev[-count].data != p.data:
                    return False  # Compara los datos de los nodos
                p = p.next
                count += 1
            return True
        else:
            return True

    def is_palindrome(self, method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()

    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head 
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next  # Encuentra el último nodo y el penúltimo nodo
            last.next = self.head  # El último nodo apunta a la cabeza
            second_to_last.next = None  # El penúltimo nodo se convierte en el último
            self.head = last  # El último nodo se convierte en la cabeza

# A -> B -> C -> D -> Null
# D -> A -> B -> C -> Null
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
llist.move_tail_to_head()
print("\n")
llist.print_list()
