import time
import sys

"""
Para cada posicion de la calculadora, en la proxima jugada solo podremos
jugar en la misma fila y columna, es decir, cuatro posibles jugadas. Para
ya tenerlo precalculado, guardamos en un diccionario las posiciones que
podemos jugar sabiendo la jugada anterior. Notemos que es independiente de
como esten dispuestos los numeros en la calculadora.
"""
jugadas_validas = {
    0: [1, 2, 3, 6],
    1: [0, 2, 4, 7],
    2: [0, 1, 5, 8],
    3: [0, 4, 5, 6],
    4: [1, 3, 5, 7],
    5: [2, 3, 4, 8],
    6: [0, 3, 7, 8],
    7: [1, 4, 6, 8],
    8: [2, 5, 6, 7]
}

meta = 31  # objetivo


def gana_pierde(contador, jugada_inicial, lista, meta):
    """
    Nos devuelve si ganamos la partida.

    Dado el valor de la calculadora, ultima tecla pulsada y la distribucion de
    las teclas.
    """
    # miramos la posicion en la calculadora de la ultima jugada
    num = -1
    for i in range(9):
        if lista[i] == jugada_inicial:
            num = i
            break

    # miramos si podemos ganar
    return int_gana_pierde(contador, num, lista, meta, {}, True)


def int_gana_pierde(contador, idx_jugada_anterior, lista, meta, prec, turno_de_quien):
    """ Recibe un estado de la partida (contador, jugada anterior y a quien le toca)
    Devuelve True si el jugador 1 gana la partida y False si la pierde.

    turno_de_quien es True si nos toca a nosotros y False si no. Por tanto, va alternando
    en cada llamada recursiva.

    prec es el diccionario de resultados precalculados. Para determinar quien gana en una jugada concreta
    unicamente importa cual es el contador, cual fue la ultima jugada realizada y por quien.
    Como clave guardamos el numero 10*contador+idx_jugada_anterior, que sirve para codificar el contador y la
    jugada realizada, porque 0<=idx_jugada_anterior<=9 (es lo mismo que guardar la tupla
    (contador,idx_jugada_anterior), pero es mas eficiente guardar un entero). Como valor, guardamos
    el numero de dos bits XY (realmente, su representacion decimal), donde Y es 0 si juega el otro y 1
    si jugamos nosotros, y X es 0 si el que juega pierde y 1 si este gana.
    """

    # si el contador >= meta, el que juega ha ganado porque el otro ha perdido
    if contador >= meta:
        return turno_de_quien

    for idx in jugadas_validas[idx_jugada_anterior]:  # miramos cada posible jugada valida

        # miramos si ya esta precalculada
        r = prec.get(10 * contador + idx)

        # si no lo esta, r sera None. Calculamos r, y guardamos 2*r+turno en el diccionario.
        if r is None:
            r = int_gana_pierde(contador + lista[idx], idx, lista, meta, prec, not turno_de_quien)
            prec[10 * contador + idx] = 2 * r + int(turno_de_quien)
        else:
            # si ya lo estaba, extraemos el valor que deberia retornar, en
            # funcion del turno con el que se habia precalculado
            quien_gana, quien_juega = r // 2, r % 2
            r = quien_gana if quien_juega == turno_de_quien else not quien_gana
            # r es True si ganamos nosotros y False si gana el otro

        # si el que juega (turno_de_quien) es el que gana la partida, gana
        if turno_de_quien == r:
            return turno_de_quien

    # si para ninguna jugada ha ganado la partida, la ha ganado el otro.
    return not turno_de_quien


# cronometramos cuanto tardamos
t0 = time.time_ns()

sys.stdin = open("recursos/entradas/entrada_modulo_2.txt", "r")
n = int(sys.stdin.readline())  # numero de partidas que se van a jugar

for i in range(n):

    linea = sys.stdin.readline().split(" ")

    # distribucion de los numeros en la calculadora
    dist = [int(linea[i]) for i in range(2, len(linea))]

    # miramos si ganamos la partida
    if gana_pierde(int(linea[0]), int(linea[1]), dist, meta):
        print("GANA")
    else:
        print("PIERDE")

print((time.time_ns() - t0) / 10 ** 9)
