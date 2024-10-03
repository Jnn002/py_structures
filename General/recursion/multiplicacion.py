# Multiplicacion con recursividad

def recursive_multiply(x, y):
    # Si y es 1, retorna x
    if y == 1:
        return x
    else:
    # Toma el valor de x, y lo suma a si mismo hasta que 'y' sea 1
        return x + recursive_multiply(x, y-1)
    
print(recursive_multiply(2, 5))