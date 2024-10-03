# Revisar si los caracteres de un string son unicos

test = 'murcielago'
test2 = 'murcielagoo'

# Usando set
#* Convertimos el string en un set y comparamos la longitud
#* Set no permite elementos duplicados
#* Si la longitud del set es igual a la longitud del string, entonces no hay elementos duplicados
def es_unico(input_str):
    return len(set(input_str)) == len(input_str)

print(f'Método 1: {es_unico(test)}')
print(f'Método 1: {es_unico(test2)}')

# Metodo iterativo
#* Evaluamos cada item de forma iterativa y guardamos en un diccionario
#* Si el item ya existe en el diccionario, retornamos False
def es_unico_2(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

print(f'Método 2: {es_unico_2(test)}')
print(f'Método 2: {es_unico_2(test2)}')
