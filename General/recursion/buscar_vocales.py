# Vocales en una palabra
#* Encontrar la cantidad de vocales en una palabra
vocales = 'aeiou'
palabra = 'Murcielago'

# Método iterativo
def buscar_vocales(palabra):
    contador_vocales = 0
    for i in range(len(palabra)):
        if palabra[i].lower() in vocales:
            contador_vocales += 1
    return f'El número de vocales en {palabra} es: {contador_vocales}'

print(f'Método iterativo: {buscar_vocales(palabra)}')

# Método recursivo
def buscar_vocales_rec(palabra):
    if palabra == '':
        return 0
    
    # Si la primera letra de la palabra no es una vocal, aumentamos el contador
    if palabra[0] not in vocales:
        return 1 + buscar_vocales_rec(palabra[1:])
    else:
    # Si la primera letra de la palabra es una vocal, no aumentamos el contador
        return buscar_vocales_rec(palabra[1:])

print(f'Método recursivo: El número de vocales en {palabra} es: {buscar_vocales_rec(palabra)}')