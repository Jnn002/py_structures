# Encontrar la longitud de nuestra cadena

palabra = 'PasteldeFresa'

def string_len(input_str):
    if input_str == '':
        return 0
    return 1 + string_len(input_str[1:])
        
print(string_len(palabra))