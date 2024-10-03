# Algoritmo que encuentra la primer letra mayuscula dentro de un string
# Iteramos sobre la paalabra y si encontramos una letra mayuscula retornamos la letra

palabra = 'videoJuegoVI'

""" def find_upperc(palabra):
    if palabra == '':
        return 'Cadena vacia'
    for i in range(len(palabra)):
        if palabra[i].isupper():
            return palabra[i]
    return f'No hay mayusculas en la palabra {palabra}'
    
print(find_upperc(palabra)) """

# Contar la cantidad de letras mayusculas en una palabra
""" def find_upperc(palabra):
    contador = 0
    if palabra == '':
        return 'Cadena vacia'
    for i in range(len(palabra)):
        if palabra[i].isupper():
            contador += 1
    return f'La cantidad de mayusculas en la palabra {palabra} es: {contador}'
    
print(find_upperc(palabra)) """

#* El problema con este tipo de algoritmos es que no son recursivos,
#* por lo que no es la mejor solucion para este tipo de problemas, puesto que 
#* se puede hacer de manera mas eficiente con recursividad

# Solucion recursiva

def find_uppercase_recursive(input_str, idx=0):
    # Si encuentra una mayuscula nos la devuelve
    if input_str[idx].isupper():
        return input_str[idx]
    # Si llegamos al final de la palabra y no encontramos mayusculas
    if idx == len(input_str) - 1:
        return "No hay mayusculas en la palabra"
    # Si no encontramos mayusculas seguimos buscando, aumentamos el indice
    return find_uppercase_recursive(input_str, idx+1)

print(find_uppercase_recursive(palabra))


