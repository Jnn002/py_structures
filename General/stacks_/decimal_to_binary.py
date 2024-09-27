from stack import Stack

def convert_int_to_bin(dec_num):
    while dec_num > 0:
        # Calcula el residuo de la división
        diferencia = dec_num % 2 # 0 o 1
        stack.push(diferencia) # Agrega el residuo a la pila
        dec_num = dec_num // 2  # Actualiza el valor de dec_num

    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())
    
    return bin_num

numero1 = 120
numero2 = 25
stack = Stack()
print(convert_int_to_bin(numero1),'\n')
print(convert_int_to_bin(numero2),'\n')