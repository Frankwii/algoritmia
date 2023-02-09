import sys

arr = [0] * 500000  # Utilizaremos este array para ir guardando los tamanos de las cascaras de encima
# de las torres. Como n<=500000, podemos simplemente inicializar este array e ir sobreescribiendolo.
idxmax = -1  # Guarda cual es la ultima posicion de arr que se esta utilizando en la actual ronda,


# Para no mezclar informacion con anteriores (se reiniciara a -1 cuando a<cabe la ronda de cangrejos)


def colocar_cangrejo(array, el):
    """Recibe el tamano de la siguiente cascara vacia y decide en que torre colocarla.
    La idea es tener las torres ordenadas por el tamano de la cascara que esta encima (las de abajo nos dan
    igual a la hora de colocar mas cascaras), en orden creciente. Para colocar una cascara vacia, busca el
    menor indice m en [0,idxmax] tal que array[m] sea mayor al tamano de la cascara y la coloca alli.
    De esta manera, se mantiene la lista ordenada: para t0do k>0, array[m-k] es menor o igual al tamano
    de la cascara (porque m es minimo), y en la nueva lista sera array[m-k]<=array[m]<=array[m+l]
    para todos k,l tales que m-k,m+l esten en [0,idxmax]. Si no existe tal indice, simplemente suma 1 a
    idxmax y coloca la cascara en array[idxmax+1].
    """
    global idxmax
    if el >= array[idxmax]:  # no existe m<=idxmax tq array[m]>el
        idxmax += 1
        array[idxmax] = el
    else:
        idx = busqueda_mayor(array, el, 0, idxmax)  # busca donde colocar el cangrejo
        array[idx] = el


# Hacemos busqueda dicotomica: log1+log2+log3+...+logn ~~ nlogn

def busqueda_mayor(lista, valor, ini, fin):
    """Busca el menor indice m en [ini,fin] tal que lista[m]>=valor, suponiendo que tal m existe.
    Esta busqueda se hace de manera dicotomica, y por tanto tiene orden logaritmico."""

    if ini >= fin:
        if fin == len(lista) - 1 and lista[-1] == valor:
            return fin
        return fin

    # Determinamos el elemento central y su valor
    mid1 = (ini + fin) // 2
    mid2 = mid1 + 1

    mid1_valor = lista[mid1]
    mid2_valor = lista[mid2]

    if mid1_valor <= valor < mid2_valor:
        return mid2

    if valor >= mid2_valor:
        # Valor esta en la parte derecha
        return busqueda_mayor(lista, valor, mid2, fin)
    if valor < mid1_valor:
        # valor esta en la parte izquierda
        return busqueda_mayor(lista, valor, ini, mid1)


sys.stdin = open("recursos/entradas/entrada_modulo_3.txt", "r")

entrada = sys.stdin.readline().split("\n")
salida = "salida_programa.txt"
sys.stdout = open(salida, "w")

while entrada[0] != '':
    num = entrada[0]
    entrada = sys.stdin.readline().split(' ')
    for i in range(int(num)):
        colocar_cangrejo(arr, int(entrada[i]))

    print(idxmax + 1)
    idxmax = -1
    arr[-1] = 0
    entrada = sys.stdin.readline().split('\n')
