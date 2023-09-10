alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# crea el diccionario {'a':0,'b':1,...,'z':25}
diccionario_posiciones = {letra: posicion for posicion, letra in enumerate(alfabeto)}
k = 26  # numero de letras en el alfabeto


def letraizq(pos, i):  # encuentra la letra que debe estar a la izquierda de la palabra en la posición pos de un lenguaje con máximo i letras.
    # En cada iteracion las palabras tienen un max de i caracteres y min de 1, por simetría hay las mismas palabras que empiezan por cada letra.
    # En total hay 26 + 26**2 + ... + 26**i = 26( 1 + 26 + ... + 26**(i-1)) = 26*t (suc. geom) palabras, k=26 son las posibles letras iniciales y t el número de palabras que empiezan por una letra dada.
    t = (k**i-1)//(k-1)
    cociente = pos//t
    resto = pos % t #determinará la posición de la palabra restante al eliminar la letra izq en el lenguaje con i-1 letras como maximo.
    letra = alfabeto[cociente]
    return (letra, resto)


def number2word(p, n):
    s = ""
    i = n # i: número de caracteres restantes por determinar
    r = p-1 # para que el algoritmo funcione la primera palabra debe estar indexada por 0.
    while i > 0:
        (letra, resto) = letraizq(r, i)
        s += letra
        i += -1
        if resto == 0:  #si el resto es 0 significa que la cadena restante es la vacía (la primera palabra del lenguaje con el caracter izquierdo eliminado). El algoritmo ha terminado, se han encontrado todos los carácteres de la palabra.
            break
        else:
            r = resto-1 #se ha eliminado la palabra vacía y ahora se recorren todos los índices en uno, la primera palabra (pos 0) ahora es 'a'.
    return s


def word2number(w, n): #la fórmula se obtiene de invertir la función number2word. 
    i = 0 #indexa la posición del caracter en la cadena empezando por la izquierda
    suma = len(w)
    for j in w:
        t = (k**(n-i)-1)//(k-1) #peso de la posicion
        suma += diccionario_posiciones[j]*t
        i += 1
    return suma
