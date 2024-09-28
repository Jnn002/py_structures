""" 
# Lista que simula un entero
A = [1, 4, 9]
# Convertir nuestra lista en un string
s = ''.join(map(str, A))
# Convertir el string en un entero y sumarle 2
print(int(s) + 2) 
"""

#* Sumar 1 número a una lista

A1 = [9, 9, 9]

def sumador(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        print(A1) # helper, para ver el proceso
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(sumador(A1))

# Estructura función map
# map(funcion, iterable)
""" 
def palabra(word):
    return word.upper()

diccionario = ['HOLA', 'Mundo', 'pythoN']

print(list(map(len, diccionario))) 
"""


