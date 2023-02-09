import sys


def caminos_totales(tablero, dimtablero):
    """Devuelve el numero de caminos desde el (0,0) hasta el (n-1,n-1) sin pasar por ninguna casilla
    en obras, teniendo en cuenta que el numero de caminos posibles hasta una casilla es la suma del
    numero de caminos posibles hasta la casilla de la izquierda y el numero de caminos posibles hasta
    la casilla de la derecha.
    """

    # Preparamos la fila y la columna de abajo: 1 solo camino si se puede llegar y 0 si hay obras en medio:
    for i in range(1, dimtablero):
        tablero[0][i] *= tablero[0][i - 1]
        tablero[i][0] *= tablero[i - 1][0]

    # Preparamos ahora el resto del tablero
    for i in range(1, dimtablero):
        for j in range(1, dimtablero):
            tablero[i][j] *= (tablero[i - 1][j] + tablero[i][j - 1])
            # Es 0 si habia obras y la suma correspondiente si no las habia
    return tablero[dimtablero - 1][dimtablero - 1]


def print_tablero(tablero, N, M):
    """Imprime un tablero de N filas y M columnas, suponiendo que tablero es un array de arrays y que el primer array
    es la fila de mas abajo.
    """

    for i in range(N - 1, -1, -1):
        string = ""
        for j in range(M):
            if tablero[i][j]:
                string += "."
            else:
                string += "X"
        print(string)
    return True


sys.stdin = open("recursos/entradas/entrada_modulo_4.txt", "r")

n = int(sys.stdin.readline().split("\n")[0])
while n != 0:
    tablero = [[1] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if sys.stdin.read(1) == "X":
                tablero[i][j] = 0
        sys.stdin.read(1)  # salto de linea

    # print_tablero(tablero, n, n)

    if tablero[0][0] == 0 or tablero[n - 1][n - 1] == 0:
        print("TABLERO IMPOSIBLE")
    else:
        print(caminos_totales(tablero, n))

    n = int(sys.stdin.readline().split("\n")[0])
