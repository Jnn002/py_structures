def find(A, target):
    # Inicializa los límites inferior y superior para la búsqueda binaria
    low = 0
    high = len(A) - 1

    while low <= high:
        # Calcula el índice medio
        mid = (low + high) // 2

        # Si el elemento medio es menor que el objetivo, ajusta el límite inferior
        if A[mid] < target:
            low = mid + 1
            # Si el elemento medio es mayor que el objetivo, ajusta el límite superior
        elif A[mid] > target:
            high = mid - 1
            # Si se encuentra el objetivo, verifica si es la primera aparición
        else:
            # Ajusta el límite superior para seguir buscando hacia la izquierda
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 285
x = find(A, target)
print(x)