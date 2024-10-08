# Primer approach
palabra = 'somos o no somos'

def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    return palabra == palabra[::-1]

print(palindromo(palabra))


# Segundo approach
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        i += 1
        j -= 1
    return True

s = 'somos o no somos'
print(is_palindrome(s))
