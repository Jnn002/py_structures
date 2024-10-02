# Encontrar un número que elevado al cuadrado seá el más cercano a un número dado

def integer_square_root(k):
    low = 0
    high = k
    
    # Ejecutar mientras low al cuadrado sea menor o igual a k
    while low**2 <= k:
        mid = (low + high) // 2
        #print('Punto medio:', mid)
        # Si mid al cuadrado es menor que k, ajusta el límite inferior
        if mid**2 < k:
            low = mid + 1
            #print('Limite menor',low)
        else:
        # Si mid al cuadrado es mayor que k, ajusta el límite superior
            high = mid - 1 
            #print('Limite mayor', high)
    return f'El resultado es: {low - 1}'

print(integer_square_root(18))
    