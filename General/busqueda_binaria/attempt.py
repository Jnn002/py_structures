A1 = [1, 2, 4, 5, 6, 6, 8, 9]

def find_closest_num(A, target):
    min_diff = min_diff_left = min_diff_right = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    # Casos especiales para lista vacía o lista
    # con solo un elemento:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high)//2

        # Asegúrate de no leer más allá de los límites de la lista.
        if mid+1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # Verifica si el valor absoluto entre los elementos
        # izquierdo y derecho es menor que cualquier otro
        # visto anteriormente.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Mueve el punto medio apropiadamente como se hace
        # en la búsqueda binaria.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        # Si el elemento en sí es el objetivo, el número más
        # cercano a él es el mismo. Devuelve el número.
        else:
            return A[mid]
    return closest_num


print(find_closest_num(A1, 11))