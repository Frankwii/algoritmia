**Problema 4**

Se tiene un tablero de tamaño (N+1)x(N+1) en el que determinadas casillas conocidas
no son transitables. Se quiere ir desde la casilla (0,0) hasta la (N,N) moviéndose
solo hacia la derecha y hacia arriba y sin pasar por casillas no transitables.
Es decir, se permiten los movimientos

                (a,b)->(a+1,b) y (a,b)->(a,b+1), siempre que las casillas sean transitables

El objetivo es determinar cuántos caminos válidos existen desde (0,0) hasta (N,M).

Se recibe un fichero con varios casos de prueba donde se indica el valor de N 
(entre 1 y 15) y una representación del tablero con caracteres "." en las casillas
transitables y "X" en las no transitables. Como salida, se debe imprimir el número
correspondiente a cada caso de prueba.

**Resolución**

Para modelizar el tablero utilizamos un array bidimensional de tamaño NxN. Inicialmente,
leemos el tablero y colocamos un 1 en las casillas transitables y un 0 en las no
transitables.

Es posible calcular el número de caminos posibles con una sencilla observación: 
para poder llegar a una casilla transitable, o bien se llega desde la casilla de abajo
o bien desde la casilla de la izquierda. Entonces, el número de caminos hasta la casilla
será la suma de los números de caminos hasta esas otras dos. Podemos, entonces, ir
calculando dicho número para cada casilla en un orden que nos permita reutilizar la
información ya calculada, hasta llegar a la casilla (N,N). Como casos base, están las casillas de la columna 0 y las de la fila 0, cuyo número de
caminos será igual al de la casilla anterior en la columna o fila (respectivamente),
si son transitables.

Para lidiar con las casillas no transitables, basta tener en cuenta que si su valor
es 0, no añadirá ningún camino a las casillas de arriba y de la derecha (como debe
ser). Simplemente, debemos tener cuidado de no modificar el valor de 0 al ir calculando.
Esto se consigue multiplicando por el valor previo de la casilla, que si no era transitable
era 0, y por tanto el valor seguirá siendo 0; y si era transitable será 1, así que
no modificará la suma correspondiente.

**Coste computacional**

Con este algoritmo, el cálculo del número de caminos hasta una casilla es siempre una
simple multiplicación y una suma. Es decir, se hacen exactamente 2 operaciones. Como
se miran todas las casillas una única vez, el coste computacional es de O(2N^2)=O(N^2).
