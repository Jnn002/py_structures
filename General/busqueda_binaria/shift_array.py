# Shifted arrary, find the smallest element index

A = [4, 5, 6, 7, 8, 1, 2, 3]

def find(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        # Si el elemento medio es menor que el elemento anterior, entonces es el mínimo
        if A[mid] < A[mid - 1]:
            return f'El índice del elemento más pequeño es: {mid} cuyo valor es {A[mid]} '
            

        # Si el elemento medio es menor que el último elemento, ajusta el límite superior
        if A[mid] < A[high]:
            high = mid - 1

        # Si el elemento medio es mayor que el último elemento, ajusta el límite inferior
        else:
            low = mid + 1

print(find(A))