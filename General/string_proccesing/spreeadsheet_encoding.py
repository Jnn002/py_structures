# Funcion 'ord()' nos da el valor ASCII de un caracter
# al usar ord('A') - ord('A') + 1, estamos obteniendo el valor de la columna A = 1
# al usar ord('B') - ord('A') + 1, estamos obteniendo el valor de la columna B = 2
# al usar ord('Z') - ord('A') + 1, estamos obteniendo el valor de la columna C = 26

def spreadsheet_encode_column(col_str):
    num = 0
    # Asignamos la longitud de nuestra cadena  a count, que nos servira como exponente
    count = len(col_str) - 1
    
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
    # Decrementamos count para que el exponente disminuya
        count -= 1
    return num

print(spreadsheet_encode_column("ZZ"))

