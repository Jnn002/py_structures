# Encontrar la longitud de nuestra cadena

palabra = 'PasteldeFresa'

# Metodo iterativo

def string_len_iter(input_str):
    contador = 0
    for i in input_str:
        contador += 1
    return contador

print(f'Método iterativo: {string_len_iter(palabra)}')

# Metodo recursivo
def string_len(input_str):
    if input_str == '':
        return 0
    return 1 + string_len(input_str[1:])
        
print(f'Método recursivo: {string_len(palabra)}')
