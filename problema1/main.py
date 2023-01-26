import sys
import time


def busqueda_ultima_posidonia(tablero, N, M, K, n, lposidonias):
    """Suponemos que hay algun camino con el tablero lleno. El metodo hace una busqueda
    dicotomica sobre la lista de posidonias para averiguar cual es la ultima que se puede
    quitar.

    Para comprobar si existe camino al quitar la posidonia m-esima, debemos quitar las m
    primeras posidonias. Si existe camino, es que la ultima posidonia tiene posicion >m,
    y por tanto podemos descartar la primera mitad de la lista y dejar quitadas esas posidonias.
    Si no existe, es que la ultima posidonia tiene posicion <m. Luego, cuando nos
    situemos en el centro del nuevo intervalo, debemos volver a colocar las posidonias que
    van despues de el.
    """

    mid = (n - 1) // 2  # Empezamos la busqueda dicotomica antes para poder preparar el tablero

    for i in range(mid + 1):
        x, y = lposidonias[i]
        tablero[x][y] = 0

    return int_busqueda_ultima_posidonia(tablero, N, M, K, lposidonias, 0, n - 1, mid)


def int_busqueda_ultima_posidonia(tablero, N, M, K, lposidonias, ini, fin, mid):
    """Subrutina auxiliar para llevar a cabo la busqueda dicotomica."""
    if ini == fin - 1:
        return fin

    if buscar_camino(tablero, N, M, K, K * K):  # La ultima esta a la derecha
        ini = mid
        mid = (ini + fin) // 2
        # Preparamos el tablero
        for i in range(ini + 1, mid + 1):  # Fuera de [ini+1:mid+1] ya esta preparado para la proxima iteracion
            x, y = lposidonias[i]  # Quitamos la posidonia antes de mid (incluido)
            tablero[x][y] = 0
        return int_busqueda_ultima_posidonia(tablero, N, M, K, lposidonias, ini, fin, mid)
    else:  # La ultima esta a la izquierda
        fin = mid
        mid = (ini + fin) // 2
        # Preparamos el tablero
        for i in range(mid + 1, fin + 1):  # Fuera [mid+1:fin+1] ya esta preparado para la proxima iteracion
            x, y = lposidonias[i]  # Volvemos a colocar la posidonia despues de mid (no incluido)
            tablero[x][y] = 1

        return int_busqueda_ultima_posidonia(tablero, N, M, K, lposidonias, ini, fin, mid)


def buscar_camino(tablero, N, M, K, K2):  # K2=K**2; se pasa por parametro para no tener que calcularlo cada vez
    """Determina, dado un tablero de (N+1)x(M+1) y una distancia K, si hay algun camino del
    punto (0,0) hasta el punto (N,M). Para hacerlo, se centra en una casilla con posidonia
    - inicalmente, (0,0) - y mira todas las casillas con posidonia a las que puede acceder
    la foca desde alli. Las anade a una pila para posteriormente mirar sus vecinos, y las
    marca con un 2 para no volverlas a mirar de nuevo. Cada vez que se centra en una casilla
    la elimina de la pila, y como esta marcada con 2 no la volvera a anadir. Por eso es util
    marcar (0,0) con un 2 nada mas empezar (si no, miraria sus vecinos dos veces).

    Guarda las casillas visitadas en la variable "listavisitados", para, antes de acabar,
    devolver el tablero a su estado inicial.
    """

    pila = [(0, 0)]
    listavisitados = []

    long_pila = 1  # len(pila); lo vamos a ir actualizando a mano para ahorrar coste

    while long_pila != 0:
        x, y = pila.pop(0)
        long_pila -= 1

        """Como solo nos interesan las casillas con posidonia a distancia <= K de (x,y),
        no es necesario mirar todo el tablero: es suficiente comprobar el cuadrado
        circunscrito a la circunferencia de radio K centrada en (x,y), es decir, el cuadrado
        de apotema K centrado en (x,y).
        """

        liminfx = max(x - K, 0)  # Hay que restringir el cuadrado a las dimensiones del tablero
        limsupx = min(x + K, N)
        liminfy = max(y - K, 0)
        limsupy = min(y + K, M)

        for i in range(liminfx, limsupx + 1):
            for j in range(liminfy, limsupy + 1):

                if tablero[i][j] == 1 and (x - i) ** 2 + (y - j) ** 2 <= K2:
                    pila.insert(0, (i, j))
                    long_pila += 1
                    listavisitados.append((i, j))
                    tablero[i][j] = 2
                    if (i, j) == (N, M):
                        for a, b in listavisitados:  # Devolvemos el tablero a su estado inicial
                            tablero[a][b] = 1
                        return True

    # Si sale del bucle sin haber devuelto nada es que no ha encontrado camino
    for a, b in listavisitados:  # Devolvemos el tablero a su estado inicial
        tablero[a][b] = 1
    return False


sys.stdin = open("recursos/entradas/parametros_coordenadas.txt", "r")

entrada = sys.stdin.readline().split(" ")

t0 = time.time_ns()
while len(entrada) == 4:

    N = int(entrada[0])
    M = int(entrada[1])
    K = int(entrada[2])
    n = int(entrada[3])

    # Inicializamos el tablero de casillas, en principio, todas vacias.
    tablero = []
    for i in range(N + 1):
        tablero.append([])
        for j in range(M + 1):
            tablero[i].append(0)

    # Sembramos la posidonia
    posidonia = [(0, 0)] * n
    for i in range(n):
        entrada = sys.stdin.readline().split(" ")
        x = int(entrada[0])
        y = int(entrada[1])

        if x < 0 or x > N or y < 0 or y > M:
            print("ERROR: posidonia fuera del tablero")
            break
        if tablero[x][y] == 1:
            print("ERROR: posidonia dos veces")
            break

        tablero[x][y] = 1

        posidonia[i] = (x, y)

    tablero[0][0] = 2  # Reduce coste. La razon se explica en el docstring de "buscar_camino".
    tablero[N][M] = 1

    if not buscar_camino(tablero, N, M, K, K * K):
        print("NUNCA SE PUDO")

    else:
        x, y = posidonia[busqueda_ultima_posidonia(tablero, N, M, K, n, posidonia)]
        print(x, y)

    entrada = sys.stdin.readline().split(" ")
print((time.time_ns() - t0) / (10 ** 9))
